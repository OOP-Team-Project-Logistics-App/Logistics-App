class Truck:
    def __init__(self, id: int, name: str, capacity: int, max_range: int):
        self.id = id
        self._name = name
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

    @classmethod
    def print_trucks(cls, truck_dict):
        for truck_id, truck in truck_dict.items():
            print(
                f"Truck ID: {truck_id}, Name: {truck.name}, Capacity: {truck.capacity} kg, Max Range: {truck.max_range} km")


trucks = [Truck(1001 + i, "Scania", 42000, 8000) for i in range(10)] + \
              [Truck(1011 + i, "Man", 37000, 10000) for i in range(15)] + \
              [Truck(1026 + i, "Actros", 26000, 13000) for i in range(15)]
truck_dict = {truck.id: truck for truck in trucks}

Truck.print_trucks(truck_dict)
