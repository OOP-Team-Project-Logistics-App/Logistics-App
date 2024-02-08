from datetime import datetime, timedelta
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

    def total_distance(self):
        total = 0
        for i in range(len(self.locations) - 1):
            total += Distance.find_distance(self.locations[i], self.locations[i + 1])
        return total
    
    def calculate_travel_time(self, departure_city, arrival_city):
        speed = 87
        distance = Distance.find_distance(departure_city, arrival_city)
        time = distance / speed
        return timedelta(hours=time)
    
    def format_date(self, date):
        suffix_list = ["th", "st", "nd", "rd"] + ["th"] * 6
        day = date.day
        if 11 <= day <= 13:
            suffix = "th"
        else:
            suffix = suffix_list[day % 10]
        formatted_date = date.strftime(f"%b {day}{suffix} %H:%Mh")
        return formatted_date
    
    def total_weight(self):
        return sum(package.weight for package in self.packages)
    
    def route_info(self):
        departure_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 6) + timedelta(days=1)
        output_string = f"Route {self._id}: "
        for i in range(len(self._locations) - 1):
            arrival_time = departure_time + self.calculate_travel_time(self._locations[i], self._locations[i + 1])
            output_string += f"{self._locations[i]} ({self.format_date(departure_time)}) -> "
            departure_time = arrival_time
        return output_string + f"{self._locations[-1]} ({self.format_date(departure_time)})"

    def __str__(self):
        return f"Route {self._id}: {' -> '.join(self._locations)} created."