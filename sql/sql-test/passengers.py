import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("database_url"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    # Show all flights
    flights = db.execute("SELECT id, origin, destination, duration FROM flights").fetchall()
    for flight in flights:
        print(f"Flight {flight.id}: from {flight.origin} to {flight.destination}, lasting {flight.duration} minutes.")

    # Prompt users to select a flight
    flight_id = int(input("\nFlight ID: "))
    # Never trust input from users, use :placeholder to make data secure to database
    flight = db.execute("SELECT * FROM flights WHERE flights.id = :id",
         {"id": flight_id}).fetchone()

    if flight is None:
        print("Error: the flight doesn't exist!")
        return
    
    passengers = db.execute("SELECT name FROM passengers WHERE passengers.flight_id = :id",
         {"id": flight_id}).fetchall()
    
    if len(passengers) == 0:
        print(f"No passenger has ordered the flight {flight_id}")
        return
    
    print("Passengers: ")
    for passenger in passengers:
        print(passenger.name)    

if __name__ == "__main__":
    main()