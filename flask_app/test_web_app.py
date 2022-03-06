import web_app
import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


## Create a pytest fixture that configure the application for testing. 
@pytest.fixture
def client():
    app = web_app.app
    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as client:
            yield client

## Test if the site is working for "/" route and "/predict" post route.
## Test if the get route for "/predict" redirect corretly.
def test_status(client):
    mp = client.get("/")
    assert mp.status_code == 200
    pred = client.get("/predict")
    assert pred.status_code == 302
    predicted = client.post('/predict', data={"sentence":"This is a test sentence."})
    assert predicted.status_code == 200

##Test if the site is rendering the correct html page:
def test_html(client):
    mp = client.get("/")
    assert b'<!DOCTYPE html>' in mp.data
    assert b'<title>Toxicity Analysis</title>' in mp.data
    predicted = client.post('/predict', data={"sentence":"This is a test sentence."})
    assert b'<!DOCTYPE html>' in mp.data
    assert b'<title>Toxicity Analysis</title>' in mp.data

## Test if the site returns the correct prediction when sending sentence to analyse.
def test_predic(client):
    pred_pos = client.post('/predict', data={"sentence":"This is a shit test sentence!"})
    assert b'Toxicity' in pred_pos.data
    assert b'Severe toxicity' in pred_pos.data
    assert b'Obscene' in pred_pos.data
    assert b'Threat' in pred_pos.data
    assert b'Insult' in pred_pos.data
    assert b'Identity' in pred_pos.data

## Test if the application can handle 100 requests on index in less than 60 secondes.
def test_stress_home(client):
    start = time.time()
    for i in range(100):
        client.get('/')
        end = time.time()
    end = time.time()
    recorded_time = start - end
    assert recorded_time < 60

## Test if the application can handle 100 prediction in less than 60 secondes.
def test_stress_prediction(client):
    recorded_time = []
    pred_test = "This is a stress test"
    start = time.time()
    for i in range(100):
        client.post('/predict', data={"sentence":pred_test})
    end = time.time()
    recorded_time = start - end
    assert recorded_time < 60

##End-to-End testing of clicking the submit button.
def test_click_submit(client):
    s=Service(ChromeDriverManager().install())    
    driver = webdriver.Chrome(service=s) 
    driver.get("http://127.0.0.1:5000/")
    submit = driver.find_element(By.TAG_NAME, "textarea")
    button = driver.find_element(By.CLASS_NAME, "bn30")
    submit.send_keys('This is a shit test sentence')
    button.click()
    result = driver.find_element(By.ID, "result")
    driver.quit()
    assert result
