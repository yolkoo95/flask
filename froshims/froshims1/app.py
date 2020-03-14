from flask import Flask, redirect, render_template, request

app = Flask(__name__)

students = []

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/registrant")
def registrant():
	return render_template("registered.html", students=students)

@app.route("/register", methods=["POST"])
def register():
	name = request.form.get("name") # if method is 'GET', xxx = request.args.get("xxx")
	dorm = request.form.get("dorm") # if method is 'POST', xxx = request.form.get("xxx")
	if not name or not dorm:
		return render_template("failure.html")
	
	students.append("%s from %s" %(name, dorm))
	return redirect("/registrant")
