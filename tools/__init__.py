import openrouteservice as ors
from openrouteservice import convert
from config import API_KEY #Create config file
import json
from hashlib import sha256
from datetime import datetime
now = datetime.now()

client = ors.Client(key=API_KEY) # Specify your personal API key

class Driver:
    def __init__(self, name, car_make_model, rating, seats_available, current_route):
        self.name = name  # String: Name of the driver
        self.car_make_model = car_make_model  # String: Make and model of the driver's car
        self.rating = rating  # Integer: Driver's rating
        self.passengers = [] #List of Users
        self.seats_available = seats_available#Integer: Number of available seats
        self.seats_taken = 1 #Integer: Number of Users on route
        self.current_route = current_route  # HitchRoute object: Current route the driver is on

    def add_passenger(self, coordinate):
        self.route.append(coordinate)

    def __str__(self):
        return f"Name: {self.name}\nCar Make/Model: {self.car_make_model}\nRating: {self.rating}\nSeats Available: {self.seats_available}\nCurrent Route: {self.current_route}"

class Coordinate:
    def __init__(self, address, longitude=None, latitude=None):
        self.address = address #String: Address
        self.longitude = longitude  # Integer: Longitude coordinate
        self.latitude = latitude    # Integer: Latitude coordinate

    def geocode(self, country): #searches user's country for matching addresses
        self.longitude,self.latitude = ors.geocode.pelias_search(client,self.address,country="US")["features"][0]["geometry"]["coordinates"]
        return(self.longitude,self.latitude)

class QueuedRoute:
    def __init__(self, start_point, end_point):
        self.start_point = start_point  # Coordinate: Starting point of the route
        self.end_point = end_point      # Coordinate: Ending point of the route

    def __str__(self):
        return f"Start Point: ({self.start_point.longitude}, {self.start_point.latitude})\nEnd Point: ({self.end_point.longitude}, {self.end_point.latitude})"

class HitchRoute:
    def __init__(self, start_point, end_point, group_tolerance, hitchhost, scheduled_time=None):
        self.start_point = start_point  # Coordinate: Starting point of the route
        self.end_point = end_point      # Coordinate: Ending point of the route
        self.current_point = start_point  # Initialize current point to the starting point
        self.driver = None              # Driver: Driver assigned to the hitch route
        self.route = []                 # List of Coordinates: Derived from ORS API
        self.queue = []                 # List of Hitch Requests
        self.scheduled_time = scheduled_time if scheduled_time else now.time()  # Integer: Scheduled time for the ride (optional, default: current time)

    def add_route_coordinate(self, coordinate):
        self.route.append(coordinate)

    def approve_hitch_request(self,index):
        if self.driver.seats_taken < self.driver.seats_available:
            pass #reject request


    def add_hitch_request(self, QueuedRoute):
        if self.driver.seats_taken < self.driver.seats_available:
            #calculate detour time for QueuedRoute, use travelling salesman to calculate total time to hit Queued route points and comparing that to normal time
            self.queue.append({
                "Queued Route":QueuedRoute,
                "Detour Time":5
                })
        else:
            print("Cannot add hitch request")

    def set_driver(self, driver):
        self.driver = driver

    def set_current_point(self, current_point):
        self.current_point = current_point

    def __str__(self):
        return f"Start Point: ({self.start_point.longitude}, {self.start_point.latitude})\n" \
               f"End Point: ({self.end_point.longitude}, {self.end_point.latitude})\n" \
               f"Current Point: ({self.current_point.longitude}, {self.current_point.latitude})\n" \
               f"Driver: {self.driver}\n" \
               f"Group Tolerance: {self.group_tolerance}\n" \
               f"Scheduled Time: {self.scheduled_time}\n" \
               f"Route: {self.route}\n" \
               f"Hitch Requests: {self.queue}"
    
class User:
    def __init__(self, username, password, email, country_of_residence):
        self.username = username  # String: User's username
        self.password = User.encode(password)  # String: User's password (encrypted)
        self.email = email        # String: User's email address
        self.country_of_residence = country_of_residence  # String: User's country of residence

    def encode(key):
        return sha256(key.encode('utf-8')).hexdigest() #SHA 256: encryption method
    
    def check_password(self,psd):
        return User.encode(psd) == self.password#Security
    
    def __str__(self):
        return f"Username: {self.username}\nEmail: {self.email}\nCountry of Residence: {self.country_of_residence}"

def calculate_route(hitchroute):
    coords = [hitchroute.start_point] + hitchroute.route + [hitchroute.end_point]
    client = ors.Client(key=API_KEY)                              # create the client for ors with API key
    routes = client.directions(client, coords)                    # returns the optimized route as a polyline that needs to be decoded

    geometry = client.directions(coords)['routes'][0]['geometry'] # the two lines below decode the polyline into a dictionary
    decoded = convert.decode_polyline(geometry)
    return decoded

# Example usage:
if __name__ == "__main__":
    route1 = Route("Home", "Work")
    driver1 = Driver("John Doe", "Toyota Camry", 4.5, 3, route1)

    print(driver1)

    hitchroute1 = HitchRoute((8, 28), (3, 7), None, None)
    coords = ((8, 10), (12, 30))

    print(calculate_route(hitchroute1))

