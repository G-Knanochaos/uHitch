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
