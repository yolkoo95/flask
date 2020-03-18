from flask import Flask, request, render_template, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

notes = [] # initialization

@app.route("/", methods=["GET", "POST"])
def index():
    if session.get("notes") is None: # session initialization: session works like multithreads
        session["notes"] = []

    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)

    return render_template("index.html", notes=session["notes"])