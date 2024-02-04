from models.constants.distances import Distance


class Route:
    id = 0

    def __init__(self, start_location, start_time):
        Route.id += 1
        self._id = Route.id
        self._start_location = start_location
        self._start_time = start_time
        self.locations = {start_location: start_time}
        self._assigned_truck = []
    
    @property
    def id(self):
        return self._id
    
    @property
    def start_location(self):
        return self._start_location
    
    @property 
    def start_time(self):
        return self._start_time
    
    @property
    def assigned_truck(self):
        return tuple(self._assigned_truck)

    def add_location(self, location, time):
        if location not in self.locations:
            self.locations[location] = time
        raise ValueError("Location is already part of the route.")

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
        self._assigned_truck.append(truck.id)

    def route_info(self):
        #temporary f-string
        return f"Route {self.id}: {self.start_location} at {self.start_time} with truck {self.assigned_truck}."