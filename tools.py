import openrouteservice as ors
from openrouteservice import convert
from hashlib import sha256
from datetime import datetime
now = datetime.now()
from config import API_KEY

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

#needed
def geocode(address,country): #searches user's country for matching addresses
    return (ors.geocode.pelias_search(client,address,country="US")["features"][0]["geometry"]["coordinates"])
    #returns tuple containing (longitude,latitude)

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

def hitch_time_difference(hitchroute, queued):
    rcoords = tuple(hitchroute.route) # rcoords are the coordinates that refer to the coordinates that need to be reached for the hitches you accept; it
                                      # needs to be a tuple to be used
    
    og_coords = ((hitchroute.current_point,) + rcoords + (hitchroute.end_point,)) # coordinates for the original route
    new_coords = ((hitchroute.current_point, queued.start_point) + rcoords + (queued.end_point, hitchroute.end_point)) # coordinates for the new route
    
    og_route_duration = client.directions(client, og_coords)["summary"]["duration"] # returns the optimized route time for the original route
    new_route_duration = client.directions(client, new_coords)["summary"]["duration"] # returns the optimized route time for the new route

    return new_route_duration - og_route_duration

def group_hitch(hitch, hitchroutes, max_delay):
    rcoords = tuple(hitchroute.route)  
    
    for hitchroute in hitchroutes:
        og_coords = ((hitchroute.current_point,) + rcoords + (hitchroute.end_point,)) # coordinates for the original route
        new_coords = ((hitchroute.current_point, hitch.start_point) + rcoords + (hitch.end_point, hitchroute.end_point)) # coordinates for the new route
        
        og_route_duration = client.directions(client, og_coords)["summary"]["duration"] # returns the optimized route time for the original route
        new_route_duration = client.directions(client, new_coords)["summary"]["duration"] # returns the optimized route time for the new route

    diff = new_route_duration, og_route_duration

# Example usage:
if __name__ == "__main__":

    hitchroute1 = HitchRoute((8, 28), (3, 7), None, None)
    queue1 = QueuedRoute((8, 10), (12, 30))

    print(hitch_time_difference(hitchroute1, queue1))

