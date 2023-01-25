from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, @the_lone_wolf._"

