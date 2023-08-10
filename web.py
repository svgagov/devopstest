from flask import- flask
from flask import render_template

app = flask(__name__)

@app.route("/")
def home():
    return "Hello World"

if __name__=="__main__":
    app.run(host='0.0.0.0')
    