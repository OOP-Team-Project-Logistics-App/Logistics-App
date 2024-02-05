class Truck:
    def __init__(self, id: int, name: str, capacity: float, max_range: int):
        self._id = id
        self._name = name
        self._capacity = capacity
        self._max_range = max_range

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
    def max_range(self):
        return self._max_range