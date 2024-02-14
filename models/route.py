from datetime import datetime, timedelta
from models.constants.date_and_time_data import calculate_travel_time, format_date
from models.constants.distance_data import Distance
from models.truck import Truck


class Route:
    id_count = 0

    def __init__(self, set_off_time: datetime, locations: dict, assigned_truck: Truck = None):
        self._set_off_time = set_off_time
        self._id = self.id_counter()
        self._locations = locations
        self._packages = []
        self._assigned_truck = assigned_truck
        self._arrival_time = set_off_time + timedelta(hours = self.total_distance() / 87)

    @property
    def arrival_time(self):
        return self._arrival_time

    @property
    def set_off_time(self):
        return self._set_off_time
    
    @set_off_time.setter
    def set_off_time(self, value: datetime):
        self._set_off_time = value

    @classmethod
    def id_counter(cls):
        cls.id_count += 1
        return cls.id_count

    @property
    def assigned_truck(self):
        return self._assigned_truck

    @property
    def id(self):
        return self._id
    
    @property
    def locations(self):
        return self._locations
    
    @property 
    def packages(self):
        return tuple(self._packages)

    def add_package(self, package):
        self._packages.append(package)

    def assign_truck(self, truck: Truck):
        self._assigned_truck = truck

    def total_distance(self) -> int:
        total = 0
        for i in range(len(self.locations) - 1):
            total += Distance.find_distance(tuple(self.locations)[i], tuple(self.locations)[i + 1])
        return total

    # def calculate_arrival_time(self):
    #     self._arrival_time = self.set_off_time + timedelta(hours=self.total_distance()/87)
    #     return self._arrival_time
    
    def total_weight(self):
        return sum(package.weight for package in self.packages)
    
    def route_info(self) -> str:
        """
        The method calculates and returns a string with the time when a truck departures from the start location \
        and arrival time of the end location.

            Returns:
                str: A string representation of the route's journey schedule.
        """
        locations_string = ' -> '.join(f"{key} {format_date(value)}" for key, value in self._locations.items())
        output_string = f"Route {self._id}: {locations_string}"
        return output_string

    def __str__(self):
        return f"Route {self._id}: {' -> '.join(self._locations.keys())} created."