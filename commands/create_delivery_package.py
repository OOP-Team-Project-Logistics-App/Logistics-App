from models.package import Package

class CreateDeliveryPackageCommand:
    def __init__(self, params, app_data):
        self.params = params
        self.app_data = app_data

    def execute(self):
        start_location, end_location, weight = self.params
        package = Package(start_location, end_location, int(weight))
        self.app_data.add_package(package)
        
        return str(package)