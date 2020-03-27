import os
import requests
from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO, emit

secret_key = os.urandom(24)
app = Flask(__name__)
app.config["SECRET_KEY"] = secret_key
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("submit vote")
def vote(data):
    selection = data["selection"]
    emit("announce vote", {"selection": selection}, broadcast=True)

if __name__ == '__main__':
    app.run(debug=True)
    