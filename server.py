from main import testfunc
from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello():
    f = open("./static/index.html")
    return f.read()
