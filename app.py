from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# JSON-Datenbank
user = []

@app.route('/')
def home():
    return "Backend läuft ja wirklich!"

@app.route('/api/hello')
def hello():
    return jsonify(message="Hallo von Flask bei Render, es funktioniert!")

# Route, um alle Benutzer anzuzeigen
@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users=user)

# Route, um einen neuen Benutzer hinzuzufügen
@app.route('/api/users', methods=['POST'])
def add_user():
    new_user = request.json
    if 'name' in new_user:
        user.append(new_user)
        return jsonify(message="Benutzer hinzugefügt!", user=new_user), 201
    else:
        return jsonify(message="Ungültige Daten!"), 400