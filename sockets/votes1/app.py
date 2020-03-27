import os
import requests
from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO, emit

secret_key = os.urandom(24)
app = Flask(__name__)
app.config["SECRET_KEY"] = secret_key
socketio = SocketIO(app)

votes = {"yes": 0, "no": 0, "maybe": 0}

@app.route("/")
def index():
    return render_template("index.html", votes=votes)

# data is transferred by socket communication in json format
@socketio.on("submit vote")
def vote(data):
    selection = data["selection"]
    votes[selection] += 1
    emit("vote totals", votes, broadcast=True)

if __name__ == '__main__':
    app.run(debug=True)
    