class Flight:

    counter = 1
    cnt_passengers = 0

    def __init__(self, origin, destination, duration):
        # keep track of flight id
        self.id = Flight.counter
        Flight.counter += 1

        # keep track of passengers
        self.passengers = []

        self.origin = origin
        self.destination = destination
        self.duration = duration
    
    def print_flight_info(self):
        print(f"Flight {self.id}")
        print(f"origin: {self.origin}")
        print(f"destination: {self.destination}")
        print(f"duration: {self.duration} minutes")

    def print_passengers_info(self):
        print(f"# of Passengers: {self.cnt_passengers}")
        for passenger in self.passengers:
            print(f"{passenger.name}")
    
    def add_passenger(self, passenger):
        passenger.flight_id = self.id
        self.passengers.append(passenger)

        Flight.cnt_passengers += 1

class Passengers:

    def __init__(self, name):
        self.name = name

def main():
    flight = Flight("Beijing", "Tokyo", 98)
    # flight = Flight(origin="Beijing", destination="Tokyo", duration=98) when forget the order of parameters

    p1 = Passengers("Brian")
    p2 = Passengers("Veronica")

    flight.add_passenger(p1)
    flight.add_passenger(p2)

    flight.print_flight_info()
    print()
    flight.print_passengers_info()

if __name__ == "__main__":
    main()