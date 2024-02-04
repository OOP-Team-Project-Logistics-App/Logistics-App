class Package:
    def __init__(self, id: int, start_location: str, end_location: str, weight: float, contact_info: str):
        self.id = id
        self.start_location = start_location
        self.end_location = end_location
        self.contact_info = contact_info

    def set_start_location(self):
        pass

    def set_end_location(self):
        pass

    def assign_package(self, package):
        #assign package on the certain route
        pass

    def package_weight(self):
        # Capacity must be between lower than 42000kg
        pass

    def get_contact_info(self):
        pass

    def __str__(self):
        # "{start_location} → {end_location}"
        pass