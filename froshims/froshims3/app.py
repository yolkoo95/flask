from flask import Flask, redirect, render_template, request
import csv

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
	name = request.form.get("name") # if method is 'GET', xxx = request.args.get("xxx")
	dorm = request.form.get("dorm") # if method is 'POST', xxx = request.form.get("xxx")
	if not name or not dorm:
		return render_template("failure.html")
	
	with open("registered.csv", "a") as file # instead of "file = open(...), file.close"
		writer = csv.writer(file)
		writer.writerow((name, dorm)) # a tuple of (1st col, 2nd col, ...)
	
	return render_template("success.html")

@app.route("/registered")
def registered():
	file = open("registered.csv", "r")
	reader = csv.reader(file)
	students = list(reader)
	file.close
	return render_template("registered.html", students=students)

# for publicize web application, some details could be specified.
# if __name__ == '__main__':
#	app.run(
#		host='0.0.0.0',
#		port='8080',
#		debug='true',
#	}
