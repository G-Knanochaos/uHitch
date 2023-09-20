class Driver:
    def __init__(self, name, car_make_model, rating, seats_available, current_route):
        self.name = name  # String: Name of the driver
        self.car_make_model = car_make_model  # String: Make and model of the driver's car
        self.rating = rating  # Integer: Driver's rating
        self.seats_available = seats_available  # Integer: Number of available seats in the car
        self.current_route = current_route  # Route object: Current route the driver is on

    def __str__(self):
        return f"Name: {self.name}\nCar Make/Model: {self.car_make_model}\nRating: {self.rating}\nSeats Available: {self.seats_available}\nCurrent Route: {self.current_route}"

class Route:
    def __init__(self, origin, destination):
        self.origin = origin  # Coordinate: Starting point of the route
        self.destination = destination  # Coordinate: Destination of the route

    def __str__(self):
        return f"Origin: {self.origin}\nDestination: {self.destination}"

class Coordinate:
    def __init__(self, longitude, latitude, address):
        self.longitude = longitude  # Integer: Longitude coordinate
        self.latitude = latitude    # Integer: Latitude coordinate
        self.address = ''
    
class QueuedRoute:
    def __init__(self, start_point, end_point):
        self.start_point = start_point  # Coordinate: Starting point of the route
        self.end_point = end_point      # Coordinate: Ending point of the route

    def __str__(self):
        return f"Start Point: ({self.start_point.longitude}, {self.start_point.latitude})\nEnd Point: ({self.end_point.longitude}, {self.end_point.latitude})"

class HitchRoute:
    def __init__(self, start_point, end_point, group_tolerance, scheduled_time=None):
        self.start_point = start_point  # Coordinate: Starting point of the route
        self.end_point = end_point      # Coordinate: Ending point of the route
        self.current_point = start_point  # Initialize current point to the starting point
        self.driver = None              # Driver: Driver assigned to the hitch route
        self.route = []                 # List of Coordinates: Derived from ORS API
        self.queue = []                 # List of Hitch Requests
        self.group_tolerance = group_tolerance  # Integer: Maximum number of people to share a ride with
        self.scheduled_time = scheduled_time  # Integer: Scheduled time for the ride (optional, default: current time)

    def add_route_coordinate(self, coordinate):
        self.route.append(coordinate)

    def add_hitch_request(self, hitch_request):
        self.queue.append(hitch_request)

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


# Example usage:
if __name__ == "__main__":
    route1 = Route("Home", "Work")
    driver1 = Driver("John Doe", "Toyota Camry", 4.5, 3, route1)

    print(driver1)

