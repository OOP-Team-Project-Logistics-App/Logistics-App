<<<<<<< HEAD
from models.constants.truck_status import TruckStatus


=======
>>>>>>> fab894505400dfea766df792474968ca85e115c3
class Truck:
    def __init__(self, id: int, name: str, capacity: int, max_range: int):
        self._id = id
        self._name = name
        self._capacity = capacity
        self._remaining_capacity = capacity
        self._max_range = max_range
<<<<<<< HEAD
        self._status = TruckStatus.AVAILABLE
=======
>>>>>>> fab894505400dfea766df792474968ca85e115c3
        self._assigned_time_period = None

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def capacity(self):
        return self._capacity

    @property
    def remaining_capacity(self):
        return self._remaining_capacity

    @property
    def max_range(self):
        return self._max_range
    
    @property
<<<<<<< HEAD
    def status(self):
        return self._status
=======
    def assigned(self):
        return self._assigned
>>>>>>> fab894505400dfea766df792474968ca85e115c3

    @property
    def assigned_time_period(self):
        return self._assigned_time_period

    def assign(self, time_period):
<<<<<<< HEAD
        self._status = TruckStatus.NOT_AVAILABLE
=======
>>>>>>> fab894505400dfea766df792474968ca85e115c3
        self._assigned_time_period = time_period
    
    def add_package_weight(self, package):
        if self.remaining_capacity >= package.weight:
            self._remaining_capacity -= package.weight
        raise ValueError("This package is too heavy for the truck.")
    
    def __str__(self):
        return f"ID: {self.id}, Model: {self.name}, Capacity: {self.capacity}kg, Max range: {self.max_range}km"