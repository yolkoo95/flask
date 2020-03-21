import os
import csv
from flask import Flask
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("database_url") # URI not URL!!
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DEBUG"] = True
db.init_app(app)

def main():
    with open("flights.csv", "r") as file:
        reader = csv.reader(file)
        for origin, destination, duration in reader:
            flight = Flight(origin=origin, destination=destination, duration=duration) # compare with import.py in sqlalchemy
            db.session.add(flight)
            print(f"Added flight from {origin} to {destination} lasting {duration} minutes.")
        db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()