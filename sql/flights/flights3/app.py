import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

''' Set Database Table'''
db = SQLAlchemy()

class Flight(db.Model):
    __tablename__ = "flights"
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)

    def add_passenger(self, name):
        # passenger = Passenger(!id!, name, self.id) # we don't know the id of current passenger, which is automatically assigned by database
        passenger = Passenger(name=name, flight_id=self.id) # implicitly pass value
        db.session.add(passenger)
        db.session.commit()

class Passenger(db.Model):
    __tablename__ = "passengers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False)

'''Bind to Flask Application'''
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("database_url")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DEBUG"] = True
db.init_app(app)

@app.route("/")
def index():
    flights = Flight.query.all()
    return render_template("index.html", flights=flights)

''' Book a Flight'''
@app.route("/book", methods=["POST"])
def book():
    # get form information
    name = request.form.get("name").capitalize()
    try:
        if not request.form.get("flight_id"):
            return render_template("prompt.html")
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("val_error.html", msg="Invalid flight number!")

    # make sure that the flight exists
    flight = Flight.query.get(flight_id)
    if flight == None:
        render_template("error.html", msg="No such flight with that id!")
    
    # add passenger
    flight.add_passenger(name)
    return render_template("success.html") 

''' Query Airlines '''
@app.route("/flights")
def flights():
    flights = Flight.query.all()
    if flights == None:
        return render_template("error.html", msg="No flight in database!")
    return render_template("flights.html", flights=flights)

@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    flight = Flight.query.get(flight_id)
    if flight == None:
        return render_template("error.html", msg="No such flight has been found!")
    passengers = Passenger.query.filter_by(flight_id=flight_id).all() # bool here use "=" means "=="

    return render_template("flight.html", flight=flight, passengers=passengers)