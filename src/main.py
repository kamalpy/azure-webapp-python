from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world from Azure"

app.run(host="0.0.0.0")