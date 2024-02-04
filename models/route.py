class Route:
    def __init__(self, id: int, start_location, start_time):
        self.id = id
        self.start_location
        self.start_time
        self.locations = [(start_location, start_time)]

    def departure_time(self):
        return self.locations[0][1]

    def total_distance_of_route(self):
        #total distance must be shorter than 13000km, truck assigned based on route distance and availability
        pass

    def assign_truck(self, truck):
        #assign truck to the route
        pass

    def route_info(self):
        #temporary f-string
        return f"Route {self.id}: {self.start_location} at {self.start_time} with truck {self.truck.id}."