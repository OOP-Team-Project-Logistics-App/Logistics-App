class Package:
    def __init__(self, id, start_location, end_location, contact_info):
        self.id = id
        self.start_location = start_location
        self.end_location = end_location
        pass

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

    def contact_info(self):
        pass

    def __str__(self):
        # "{start_location} → {end_location}"
        pass