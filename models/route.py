from models.constants.distances import Distance


class Route:
    id_count = 0

    def __init__(self, route_id, locations):
        self._id = route_id
        self._locations = locations
        self._packages = []

    @classmethod
    def id_counter(cls):
        cls.id_count += 1
        return cls.id_count
    
    @property
    def id(self):
        return self._id
    
    @property
    def locations(self):
        return tuple(self._locations)
    
    @property 
    def packages(self):
        return tuple(self._packages)
    
    def add_location(self, location):
        self._locations.append(location)
        
    def add_package(self, package):
        self._packages.append(package)

    def total_weight(self):
        return sum(package.weight for package in self.packages)

    def total_distance(self):
        total = 0
        for i in range(len(self.locations) - 1):
            total += Distance.find_distance(self.locations[i], self.locations[i + 1])
        return total

    def assign_truck(self, truck):
        self.truck = truck

    def __str__(self):
        return f"Route {self._id} {' -> '.join(self._locations)} created and truck with id {self.truck.id} is assigned."
