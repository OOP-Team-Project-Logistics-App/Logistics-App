class Truck:
    def __init__(self, id: int, name: str, capacity: int, max_range: int):
        self.id = id
        self.name = name
        self.capacity = capacity
        self.max_range = max_range

    @property
    def name(self):
        return self._name

    def get_vehicle__by_id(self):
        #get vehicle id
        pass
    
    def get_capacity(self):
        #get capacity of the truck
        pass
    
    def get_max_range(self):
        #get max_range of the truck
        pass