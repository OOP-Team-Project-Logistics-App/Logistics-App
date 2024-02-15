from models.constants.truck_status import TruckStatus


class Truck:
    def __init__(self, id: int, name: str, capacity: int, max_range: int):
        self._id = id
        self._name = name
        self._capacity = capacity
        self._remaining_capacity = capacity
        self._max_range = max_range
        self._status = TruckStatus.AVAILABLE
        self._assigned_time_periods = []

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
    def status(self):
        return self._status

    @property
    def assigned_time_periods(self):
        return tuple(self._assigned_time_periods)

    def assign(self, time_period):
        self._status = TruckStatus.UNAVAILABLE
        self._assigned_time_periods.append(time_period)
        self._remaining_capacity = self._capacity

    def add_package_weight(self, package):
        if self._remaining_capacity >= package.weight:
            self._remaining_capacity -= package.weight
        else:
            raise ValueError("This package is too heavy for the truck.")
        
    def remove_package_weight(self, package):
        self._remaining_capacity += package.weight
    
    def __str__(self):
        return f"ID: {self.id}, Model: {self.name}, Capacity: {self.capacity}kg, Max range: {self.max_range}km"