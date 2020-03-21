import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# user = "unico"
# password = "***"
# host = "49.234.83.62"
# port = "5505"
# dbname = "unico"

# engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{dbname}")
engine = create_engine(os.getenv("database_url"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    #  print flights
    flights = db.execute("SELECT origin, destination, duration FROM flights")
    print("Flights Info:")
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

    passengers = db.execute("SELECT name, flight_id FROM passengers")
    print("Passengers Info:")
    for passenger in passengers:
        print(f"{passenger.name}: {passenger.flight_id}")

if __name__ == "__main__":
    main()