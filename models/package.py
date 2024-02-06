from models.constants.distances import Distance


class Package:
    id_count = 0

    def __init__(self, id: int, start_location: str, end_location: str, weight: float, contact_info: str):
        self._id = id
        self._start_location = start_location
        self._end_location = end_location
        self._weight = weight
        self.contact_info = contact_info

    @classmethod
    def id_counter(cls):
        id_count += 1
        return cls.id_count

    @property
    def id(self):
        return self._id
    
    @property
    def start_location(self):
        return self._start_location\
        
    @property
    def end_location(self):
        return self._end_location

    def set_start_location(self):
        if self._start_location in Distance.cities:
            pass

    def set_end_location(self):
        if self._end_location in Distance.cities:
            pass

    def assign_package(self, package):
        pass

    @property
    def weight(self):
        return self._weight

    def get_contact_info(self):
        pass

    def __str__(self):
        return f"{self._start_location} -> {self.end_location}"