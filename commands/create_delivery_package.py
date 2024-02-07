from commands.validators.validation_helpers import try_parse_int
from models.package import Package


class CreateDeliveryPackageCommand:
    def __init__(self, params, app_data):
        self.params = params
        self.app_data = app_data

    def execute(self):
        start_location = self.params[0]
        end_location = self.params[1]
        weight = try_parse_int(self.params[2])
        new_package = Package(start_location, end_location, weight)
        self.app_data.add_package(new_package)
        
        return str(new_package)