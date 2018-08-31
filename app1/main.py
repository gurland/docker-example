from flask import Flask
app = Flask(__name__)


@app.route("/webhook1")
def hello():
    return "Hello from app1"
