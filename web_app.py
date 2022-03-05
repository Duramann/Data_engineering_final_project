from flask import Flask, render_template, request, redirect
from detoxify import Detoxify
from string import punctuation

app = Flask(__name__)

model = Detoxify('original')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == "GET":
        return redirect('/')
        
    if request.method == 'POST':
        rawtext = request.form.values()
        texte = [str(x) for x in rawtext]
        to_process = " ".join([w for w in texte])
            
        result = model.predict(to_process)
        
        printtexte = " ".join([w for w in texte])

        printresult = {}

        for key in result:
            printresult[" ".join([w for w in key.capitalize().split('_')])] = str((result[key]*100).round(2)) + '%'



        return render_template('result.html', result=printresult, topredict='The sentence to analyse was : "' + printtexte + '"')
