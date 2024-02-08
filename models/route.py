from datetime import datetime, timedelta
from models.constants.date_and_time_data import calculate_travel_time, format_date
from models.constants.distance_data import Distance
from models.truck import Truck


class Route:
    id_count = 0

    def __init__(self, locations: list[str], assigned_truck: Truck = None):
        self._id = self.id_counter()
        self._locations = locations
        self._packages = []
        self._assigned_truck = assigned_truck

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
        return tuple(self._locations)
    
    @property 
    def packages(self):
        return tuple(self._packages)
    
    def add_location(self, location):
        self._locations.append(location)
        
    def add_package(self, package):
        self._packages.append(package)

    def assign_truck(self, truck: Truck):
        self._assigned_truck = truck

    def total_distance(self) -> int:
        total = 0
        for i in range(len(self.locations) - 1):
            total += Distance.find_distance(self.locations[i], self.locations[i + 1])
        return total
    
    def total_weight(self):
        return sum(package.weight for package in self.packages)
    
    def route_info(self) -> str:
        """
        The method calculates and returns a string with the time when a truck departures from the start location \
        and arrival time of the end location. If the cities in the route are more than two, the departure time \
        and the arrival time of the in between cities match. Departure time of the start location will always be 6 AM \
        on the next day from the current one.

            Returns:
                    str: A string representation of the route's journey schedule.
        """
        departure_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 6) + timedelta(days=1)
        output_string = f"Route {self._id}: "
        for i in range(len(self._locations) - 1):
            arrival_time = departure_time + calculate_travel_time(self._locations[i], self._locations[i + 1])
            output_string += f"{self._locations[i]} ({format_date(departure_time)}) -> "
            departure_time = arrival_time
        return output_string + f"{self._locations[-1]} ({format_date(departure_time)})"

    def __str__(self):
        return f"Route {self._id}: {' -> '.join(self._locations)} created."