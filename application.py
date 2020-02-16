from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World 2!"

@app.route("test")
def world():
    return "!2 dlroW olleH"