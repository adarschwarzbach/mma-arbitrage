from flask import Flask, jsonify
import json
import time

app = Flask(__name__)
from getData import *

@app.route("/")
def index():
    payload = createJSON()
    return jsonify(payload)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)