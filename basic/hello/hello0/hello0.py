from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def greet():
	name = request.args.get("name") 
	if not name:
		name = 'world'

	return render_template("index.html", name=name)

if __name__ == '__main__':
	app.run(host='0.0.0.0')

