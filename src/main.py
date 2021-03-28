from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    qod_resp = requests.get("https://quotes.rest/qod?language=en")
    if qod_resp.status_code == 200:
        qod = qod_resp.json()
        return qod["contents"]["quotes"][0]["quote"]
    return "Hello world from Azure"
