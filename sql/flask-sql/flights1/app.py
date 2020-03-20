import os
from flask  import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine(os.getenv("database_url"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    flights = db.execute("SELECT id, origin, destination, duration FROM flights").fetchall()
    return render_template("index.html", flights=flights)

''' Book a Flight'''
@app.route("/book", methods=["POST"])
def book():
    # Get form information
    name = request.form.get("name").capitalize()
    try:
        if not request.form.get("flight_id"):
            return render_template("prompt.html")
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("val_error.html", msg="Invalid flight number!")

    # Make sure that the flight exists
    if db.execute("SELECT * FROM flights WHERE flights.id = :id", 
        {"id": flight_id}).rowcount == 0: # note that not rowcount()
        render_template("error.html", msg="No such flight with that id!")
    db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)", 
        {"name": name, "flight_id": flight_id})
    
    db.commit()

    return render_template("success.html") 

''' Query Airlines '''
@app.route("/flights")
def flights():
    flights = db.execute("SELECT * FROM flights").fetchall()
    if flights == None:
        return render_template("error.html", msg="No flight in database!")
    return render_template("flights.html", flights=flights)

@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    flight = db.execute("SELECT origin, destination, duration FROM flights WHERE flights.id = :id",
        {"id": flight_id}).fetchone()
    if flight == None:
        return render_template("error.html", msg="No such flight has been found!")
    passengers = db.execute("SELECT name FROM passengers WHERE passengers.flight_id = :id",
        {"id": flight_id}).fetchall()
    return render_template("flight.html", flight=flight, passengers=passengers)