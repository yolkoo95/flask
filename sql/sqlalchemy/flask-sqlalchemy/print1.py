import os
from flask import Flask
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("database_url")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DEBUG"] = True
db.init_app(app)

def main():
    flights = Flight.query.all() # compare with print.py in sqlalchemy
    print("Flights Info:")
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

    passengers = Passenger.query.all()
    print("Passengers Info:")
    for passenger in passengers:
        print(f"{passenger.name}: {passenger.flight_id}")
    
if __name__ == "__main__":
    with app.app_context():
        main()