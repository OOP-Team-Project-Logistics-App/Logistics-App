from models.scania import Scania
from models.man import Man
from models.actros import Actros


class Package:
    def __init__(self, id: int, start_location: str, end_location: str, weight: float, contact_info: str):
        self._id = id
        self._start_location = start_location
        self.end_location = end_location
        self.weight = weight
        self.contact_info = contact_info

    @property
    def id(self):
        return self._id
    
    @property
    def start_location(self):
        return self._start_location

    def set_start_location(self):
        pass

    def set_end_location(self):
        pass

    def assign_package(self, package):
        #assign package on the certain route
        pass

    @property
    def weight(self):
        return self.weight
    
    @weight.setter
    def weight(self, value):
        if self.weight <= self.truck.capacity:
            self.weight = value
        raise ValueError("Package exceeds the truck's weight limit.")


    def get_contact_info(self):
        pass

    def __str__(self):
        return f"{self._start_location} -> {self.end_location}"