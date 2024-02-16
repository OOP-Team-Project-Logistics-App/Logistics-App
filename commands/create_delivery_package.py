from core.application_data import ApplicationData
from commands.base.base_command import BaseCommand
from commands.validators.validation_helpers import try_parse_int
from models.package import Package
from commands.validators.validation_helpers import validate_login


class CreateDeliveryPackageCommand(BaseCommand):
    def __init__(self, params: list, app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        validate_login(self.app_data, requires_login = True)
        start_location = self.params[0]
        end_location = self.params[1]
        weight = try_parse_int(self.params[2])
        contact_info = self.params[3]
        new_package = Package(start_location, end_location, weight, contact_info)
        self.app_data.add_package(new_package)
        
        return str(new_package)