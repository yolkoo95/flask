from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
	name = request.form.get("name") # if method is 'GET', xxx = request.args.get("xxx")
	dorm = request.form.get("dorm") # if method is 'POST', xxx = request.form.get("xxx")
	if not name or not dorm:
		return "failure"
	return render_template("success.html")
