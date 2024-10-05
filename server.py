from flask import Flask
app = Flask(__name__)
@app.route("/")
def landing():
    f = open("./static/index.html")
    return f.read()
