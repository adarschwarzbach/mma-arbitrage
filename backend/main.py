from flask import Flask, jsonify
import json
import time

app = Flask(__name__)
from getData import *

@app.route("/")
def info():
    payload = createJSON()
    return payload


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)