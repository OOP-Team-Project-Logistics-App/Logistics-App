from models.truck import Truck


class Man(Truck):
    def __init__(self, id: int, name: str, capacity: int, max_range: int):
        super().__init__(id, name, capacity, max_range)