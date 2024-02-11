from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from commands.update_current_day import UpdateCurrentDayCommand
from models.constants.date_and_time_data import calculate_travel_time
from models.constants.package_status import PackageStatus
from models.package import Package
from models.route import Route
from datetime import timedelta

class PackageStatusCommand(BaseCommand):
    def __init__(self, params: list, app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        pass