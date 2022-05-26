from flask import Flask, jsonify, make_response


# main = Blueprint('main',__name__)

# @main.route('/get_odds', methods=['POST'])
# def info():
#     payload = createJSON()
#     return 'Done', 201

# @main.route('/odds')
# def info():
#     payload = createJSON()
#     return payload

app = Flask(__name__)
from getData import *

@app.route("/")
@app.route("/data")
@app.route('/data', methods=['GET'])
def info():
    payload = createJSON()
    return payload


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)