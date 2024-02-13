from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData


class ViewUnassignedPackages(BaseCommand):
    def __init__(self, params: list, app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        return self.app_data.view_unassigned_packages()