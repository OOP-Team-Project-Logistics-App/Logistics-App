from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData


class PackageStatusCommand(BaseCommand):
    def __init__(self, params: list, app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        #not entirely implemented
        package_id = self.params[0]
        current_city = self.params[1]

        package = self.app_data.get_package_by_id(package_id)
        package.update_package_status(current_city)

        return f"Package {package_id} status updated to {package.status.value}."