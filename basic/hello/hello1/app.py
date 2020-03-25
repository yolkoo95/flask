from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def greet():
	name = request.args.get("name") 
	if not name:
		name = 'world'

	return render_template("index.html", name=name)

if __name__ == "__main__":
	app.run()

# if you want to run flask in terminal, you must set FLASK_APP=<filename> as follow,
# export FLASK_APP=hello1.py
# and then flask can be executed in terminal by 'flask run (--host=0.0.0.0)', host=0.0.0.0
# for public access.
