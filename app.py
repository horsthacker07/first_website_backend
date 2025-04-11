from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Backend läuft ja wirklich!"

@app.route('/api/hello')
def hello():
    return jsonify(message="Hallo von Flask bei Render!")