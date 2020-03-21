import os
from flask import Flask
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("database_url")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DEBUG"] = True
db.init_app(app)

def main():
    # query passengers of a flight
    # show all flights
    flights = Flight.query.all()
    for flight in flights:
        print(f"Flight {flight.id}: from {flight.origin} to {flight.destination}, lasting {flight.duration} minutes.")

    # prompt users to select a flight
    flight_id = int(input("\nFlight ID: "))
    flight = Flight.query.get(flight_id)
    # flight = Flight.query.filter_by(id=flight_id).first() # which is equal to the code above

    if flight is None:
        print("Error: the flight doesn't exist!")
        return
    
    passengers = Passenger.query.filter(Passenger.flight_id == flight_id).all()    
    if len(passengers) == 0:
        print(f"No passenger has ordered the flight {flight_id}")
        return
    
    print("Passengers: ")
    for passenger in passengers:
        print(passenger.name)    

if __name__ == "__main__":
    with app.app_context():
        main()