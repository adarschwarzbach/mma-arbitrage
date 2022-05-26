from flask import Flask, jsonify, make_response
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)
from getData import *


@app.route("/")
@app.route("/data")
@app.route('/data', methods=['GET'])
def info():
    payload = createJSON()
    return payload


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)