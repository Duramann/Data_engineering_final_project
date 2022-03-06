from flask import Flask, render_template, request, redirect
from detoxify import Detoxify
from prometheus_client import start_http_server, Counter, generate_latest, Histogram
from multiprocessing.pool import ThreadPool
import time

app = Flask(__name__)

model = Detoxify('original')

REQUESTS = Counter('home_total', 'Home page requested.')
PRED = Counter('prediction_total', 'Predictions done.')
PRED_TIME = Histogram('prediction_latency_seconds','Time for a prediction.')

@app.route('/')
def home():
    REQUESTS.inc()
    return render_template('index.html')


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == "GET":
        return redirect('/')
        
    if request.method == 'POST':
        start = time.time()
        rawtext = request.form.values()
        texte = [str(x) for x in rawtext]
        to_process = " ".join([w for w in texte])
            
        result = model.predict(to_process)
        
        printtexte = " ".join([w for w in texte])

        printresult = {}

        for key in result:
            printresult[" ".join([w for w in key.capitalize().split('_')])] = str((result[key]*100).round(2)) + '%'

        PRED.inc()
        PRED_TIME.observe(time.time() - start)

        return render_template('result.html', result=printresult, topredict='The sentence to analyse was : "' + printtexte + '"')

@app.route('/metrics')
def metrics():
      return generate_latest()

if __name__ == "__main__":
      pool = ThreadPool(1)
      app.run(host='0.0.0.0', port='5000')