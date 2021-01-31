from flask import Flask, request, jsonify
from flask_cors import CORS
from Model.model.py import model_prediction

app = Flask(__name__)
CORS(app)

@app.route("/", method=['POST'])
def index():
    return jsonify(model_prediction(request.get_json(force=True))), 200

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)