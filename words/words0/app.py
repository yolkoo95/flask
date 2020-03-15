from flask import Flask, render_template, request

app = Flask(__name__)

# read dictionary
dic = []
with open("/Users/Quminzhi/Documents/python/flask/words/words0/large", "r") as file:
    for line in file.readlines():
        dic.append(line.rstrip) # str.rstrip: delete ' ' on each side of str

@app.route('/')
def index():
    return render_template("index.html") 

@app.route('/search', methods=["GET"])
def search():
    q = request.args.get("query")
    if not q:
        return render_template("err_input.html")
    
    words = [word for word in dic if word.startswith(q)]
    return render_template("search.html", words=words)
