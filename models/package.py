from models.constants.distance_data import Distance


class Package:
    id_count = 0

    def __init__(self, start_location: str, end_location: str, weight: int):
        self._id = self.id_counter()
        self.start_location = start_location
        self.end_location = end_location
        self._weight = weight
        # self.contact_info = contact_info -> temporary removed as an attribute

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
        if location in Distance.cities:
            self._end_location = location
        else:
            raise ValueError("There is no hub in this city.")
    
    @property
    def weight(self):
        return self._weight

    def get_contact_info(self):
        pass

    def package_info(self):
        return f"{self.start_location} -> {self.end_location}, Weight: {self.weight}kg"
    
    def __str__(self):
        return f"Package with id {self._id} created. --\n" \
                f"-- Accepted in city: {self.start_location} --\n" \
                f"-- Delivery to: {self.end_location} --\n" \
                f"-- Weight: {self.weight}kg --"