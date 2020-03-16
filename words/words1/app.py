from flask import Flask, render_template, request

app = Flask(__name__)

# read dictionary
dic = []
with open("/Users/Quminzhi/Documents/python/flask/words/words0/large", "r") as file:
    for line in file.readlines():
        dic.append(line.rstrip()) # str.rstrip: delete ' ' on each side of str

@app.route('/')
def index():
    return render_template("index.html") 

@app.route('/search')
def search():
    q = request.args.get("query") # notice that server get query.value from js, not from form methods, referring to generator.js

    words = [word for word in dic if q and word.startswith(q)]
    return render_template("search.html", words=words)
