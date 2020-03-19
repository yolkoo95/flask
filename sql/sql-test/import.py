import csv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("database_url"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    # import data from csv into remote database
    with open("flights.csv", "r") as file:
        reader = csv.reader(file)
        for origin, destination, duration in reader:
            db.execute("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)",
            {"origin": origin, "destination": destination, "duration": duration})
            print(f"Added flight from {origin} to {destination} lasting {duration} minutes.")
    
    db.commit()

if __name__ == "__main__":
    main()