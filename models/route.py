from models.constants.distances import Distance


class Route:
    id_count = 0

    def __init__(self, id, start_location):
        self._id = id
        self._start_location = start_location
        self._locations = []
        self._assigned_truck = []

    @classmethod
    def id_counter(cls):
        cls.id_count += 1
        return cls.id_count
    
    @property
    def id(self):
        return self._id
    
    @property
    def start_location(self):
        return self._start_location
    
    @property 
    def locations(self):
        return tuple(self._locations)
    
    @property
    def assigned_truck(self):
        return tuple(self._assigned_truck)

    def add_location(self, location):
        if location not in self.locations:
            self._locations.append(location)
        else:
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
        return f"Route {self.id}: {' -> '.join(self._locations)} created."
