import os
from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("database_url") # URI not URL!!
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DEBUG"] = True
db.init_app(app) # tight db with app

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context(): # call for flask object when running application, different from request context, which calls for flask object by http request
        main()