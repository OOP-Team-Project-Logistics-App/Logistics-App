from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData


class GetPackageInformation(BaseCommand):
    def __init__(self, params: list, app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        package_id = self.params[0]
        package = self.app_data.get_package_by_id(package_id)

        return package.package_info()