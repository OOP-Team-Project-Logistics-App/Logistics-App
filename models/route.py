from models.constants.distances import Distance


class Route:
    def __init__(self, id: int, start_location, start_time):
        self.id = id
        self.start_location
        self.start_time
        self.locations = [(start_location, start_time)]

    def departure_time(self):
        return self.locations[0][1]

    def total_distance_of_route(self):
        total_distance = 0
        for i in range(len(self.locations) - 1):
            if total_distance <= 13000:
                departure_city, _ = self.locations[i]
                arrival_city, _ = self.locations[i + 1]
                total_distance += Distance.find_distance(departure_city, arrival_city)
        return total_distance

    def assign_truck(self, truck):
        if not truck.max_range > self.total_distance_of_route():
            raise ValueError("This truck cannot cover this route.")
        self.truck = truck

    def route_info(self):
        #temporary f-string
        return f"Route {self.id}: {self.start_location} at {self.start_time} with truck {self.truck.id}."