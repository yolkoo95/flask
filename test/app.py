from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
    currency = request.form.get("currency")

    # query for exchange rate
    res = requests.get("http://data.fixer.io/api/latest?access_key=34119a0aaa3d3af1b32259d9c6ec1b15",
                        params={"base": "EUR", "symbols": currency})
    
    # make sure request succeeded
    if res.status_code != 200:
        return jsonify({"success": False}), 401
    
    data = res.json()

    # make sure access to data
    if data["success"] == False:
        return jsonify({"success": False}), 402

    # make sure currency exists
    if currency not in data["rates"]:
        return jsonify({"success": False}), 403

    return jsonify({"success": True, "rate": data["rates"][currency]})

if __name__ == "__main__":
    app.run(
        debug = True
    )