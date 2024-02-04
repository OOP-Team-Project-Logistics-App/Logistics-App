class Route:
    def __init__(self, id: int, start_location, start_time):
        #
        #
        #
        self.locations = []

    def departure_time(self):
        #first_location of delivery_route has departure_time, departure time cannot be in the past
        pass

    def add_location(self, location, arrival_time):
        #location + arrival time to the location
        pass

    def total_distance_of_route(self):
        #total distance must be shorter than 13000km, truck assigned based on route distance and availability
        pass

    def assign_truck(self, truck):
        #assign truck to the route
        pass

    def route_info(self):
        #f-string info
        pass