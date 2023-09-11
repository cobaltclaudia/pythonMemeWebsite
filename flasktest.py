#!/bin/python3

from flask import Flask

app = Flask(__name__)

# WARNING: This is a development server. Do not use it in a production deployment.
@app.route("/")
def index():
    return "Yo beeeech!"


app.run(host="0.0.0.0", port=80)
