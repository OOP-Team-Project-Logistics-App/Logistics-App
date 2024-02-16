from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from commands.validators.validation_helpers import validate_login


class PackageStatusCommand(BaseCommand):
    def __init__(self, params: list, app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        validate_login(self.app_data, requires_login = True)
        package_id = self.params[0]
        current_time = self.app_data.current_day

        package = self.app_data.get_package_by_id(package_id)
        package.update_package_status(current_time)

        return f"Package {package_id} status is {package.status.value}."