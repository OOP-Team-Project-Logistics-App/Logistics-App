from models.constants.distances import Distance
from models.truck import Truck


class Route:
    id_count = 1

    def __init__(self, locations: list[str], assigned_truck: Truck = None):
        self._id = Route.id_count
        self._locations = locations
        self._packages = []
        self._assigned_truck = assigned_truck
        Route.id_count += 1


    @property
    def assigned_truck(self):
        return self._assigned_truck

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

    def total_weight(self):             #TO FIX
        return sum(package.weight for package in self.packages)

    def total_distance(self):
        total = 0
        for i in range(len(self.locations) - 1):
            total += Distance.find_distance(self.locations[i], self.locations[i + 1])
        return total

    def assign_truck(self, truck: Truck):
        self._assigned_truck = truck

    def __str__(self):
        return f"Route {self._id} {' -> '.join(self._locations)} created."
