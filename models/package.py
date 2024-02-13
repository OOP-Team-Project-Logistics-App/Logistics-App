from models.constants.date_and_time_data import calculate_travel_time
from models.constants.distance_data import Distance
from models.constants.package_status import PackageStatus
from models.route import Route


class Package:
    id_count = 0

    def __init__(self, start_location: str, end_location: str, weight: int, contact_info: str, package_assigned_route: Route = None):
        self._id = self.id_counter()
        self.start_location = start_location
        self.end_location = end_location
        self._weight = weight
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

    def update_package_status(self, current_time):
        if self._package_assigned_route is None:
            self._status = PackageStatus.NOT_ASSIGNED
        else:
            departure_time = None
            arrival_time = None
            for location, time in self._package_assigned_route.locations.items():
                if location == self._start_location:
                    departure_time = time
                if location == self._end_location:
                    arrival_time = time
            if current_time < departure_time:
                self._status = PackageStatus.PENDING
            elif arrival_time > current_time > departure_time:
                self._status = PackageStatus.EN_ROUTE
            else:
                self._status = PackageStatus.DELIVERED
        #     departure_time = self._package_assigned_route.set_off_time
        #     for i in range(len(self._package_assigned_route.locations) - 1):
        #         arrival_time = departure_time + calculate_travel_time(self._package_assigned_route.locations[i], self._package_assigned_route.locations[i + 1])
        #         if self._package_assigned_route.locations[i] == self.start_location and self._package_assigned_route.locations[i + 1] == self.end_location:
        #             if departure_time <= current_time < arrival_time:
        #                 self._status = PackageStatus.EN_ROUTE
        #             elif current_time >= arrival_time:
        #                 self._status = PackageStatus.DELIVERED

    def package_info(self):
        return f"Package ID {self._id}:\n" \
                f"{self.start_location} -> {self.end_location}\n" \
                f"Weight: {self.weight}kg\n" \
                f"Contact info: {self._contact_info}"
    
    def __str__(self):
        return f"Package with id {self._id} created. --\n" \
                f"-- Accepted in city: {self.start_location} --\n" \
                f"-- Delivery to: {self.end_location} --\n" \
                f"-- Weight: {self._weight}kg --\n" \
                f"-- Contact Info: {self.contact_info} --"