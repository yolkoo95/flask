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

'''Book a Flight'''
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
    if db.execute("SELECT * FROM flights WHERE flights.id = :id", 
        {"id": flight_id}).rowcount == 0: # note that not rowcount()
        render_template("error.html", msg="No such flight with that id!")
    
    # add passenger
    db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)", 
        {"name": name, "flight_id": flight_id}) 
    db.commit()

    return render_template("success.html") 