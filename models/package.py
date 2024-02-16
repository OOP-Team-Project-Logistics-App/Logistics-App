from datetime import datetime
from models.constants.distance_data import Distance
from models.constants.package_status import PackageStatus
from models.route import Route


class Package:
    id_count = 0

    def __init__(self, start_location: str, end_location: str, weight: int, contact_info: str, package_assigned_route: Route = None):
        self._id = self.id_counter()
        self.start_location = start_location
        self.end_location = end_location
        self.weight = weight
        self.contact_info = contact_info
        self._package_assigned_route = package_assigned_route
        self._status = PackageStatus.NOT_ASSIGNED

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
    
    @start_location.setter
    def start_location(self, location):
        if location in Distance.cities:
            self._start_location = location
        else:
            raise ValueError("There is no hub in this city.")
        
    @property
    def end_location(self):
        return self._end_location
    
    @end_location.setter
    def end_location(self, location):
        if location in Distance.cities and location != self._start_location:
            self._end_location = location
        else:
            raise ValueError("There is no hub in this city or the location is the same city.")
    
    @property
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight(self, value: int):
        if value > 0:
            self._weight = value
        else:
            raise ValueError("Weight cannot be negative.")
    
    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    def contact_info(self, info):
        if "@" in info and "." in info.split("@")[1]:
            self._contact_info = info
        else:
            raise ValueError("Invalid contact information.")
        
    @property
    def package_assigned_route(self):
        return self._package_assigned_route

    @package_assigned_route.setter
    def package_assigned_route(self, route: Route):
        self._package_assigned_route = route
        
    @property
    def status(self):
        return self._status

    #If there is no route assigned to the package, its status is "Not assigned", otherwise iterate through the route's
    #locations and their respective arrival times. If there's a match with the package's start location the route's location,
    #that location's arrival becomes the package's departure time. Do the same for the package's end location. The status
    #of the package changes depending on its progress through the route depending on the current day.
    def update_package_status(self, current_time: datetime):
        if not isinstance(current_time, datetime):
            raise ValueError("Current time must be a datetime object.")
        if self._package_assigned_route is None:
            self._status = PackageStatus.NOT_ASSIGNED
        else:
            departure_time, arrival_time = None, None
            for location, time in self._package_assigned_route.locations.items():
                if location == self._start_location:
                    departure_time = time
                if location == self._end_location:
                    arrival_time = time

            self._status = (PackageStatus.PENDING if current_time < departure_time else
                            PackageStatus.EN_ROUTE if departure_time <= current_time < arrival_time else
                            PackageStatus.DELIVERED)

    def package_info(self):
        return f"Package ID {self._id}:\n" \
                f"{self.start_location} -> {self.end_location}\n" \
                f"Weight: {self.weight}kg\n" \
                f"Contact info: {self._contact_info}"
    
    def __str__(self):
        return f"Package with id {self._id} created.\n" \
                f"-- Accepted in city: {self.start_location} --\n" \
                f"-- Delivery to: {self.end_location} --\n" \
                f"-- Weight: {self._weight}kg --\n" \
                f"-- Contact Info: {self.contact_info} --"