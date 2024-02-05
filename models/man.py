from models.truck import Truck


class Man(Truck):
    MAX_RANGE = 10000
    CAPACITY = 37000
    NAME = "MAN"

    def __init__(self, id: int):
        super().__init__(id)
        self._name = Man.NAME
        self._capacity = Man.CAPACITY
        self._max_range = Man.MAX_RANGE
        self.id = id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        if not 1011 <= id <= 1025:
            raise ValueError("Invalid truck.")


    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value != 37000:
            raise ValueError("This truck has 37000 capacity.")
        self._capacity = value

    @property
    def max_range(self):
        return self._max_range

    @max_range.setter
    def max_range(self, value):
        if value != 10000:
            raise ValueError("This truck has a maximum range of 10000.")
        self._max_range = value