from core.application_data import ApplicationData
from commands.update_current_day import UpdateCurrentDayCommand
from models.constants.date_and_time_data import calculate_travel_time
from models.constants.package_status import PackageStatus
from models.package import Package
from models.route import Route
from datetime import timedelta

class PackageStatusCommand:
    def __init__(self, params, app_data: ApplicationData):
        self.params = params
        self.app_data = app_data

    def execute(self):
        day_today = UpdateCurrentDayCommand.current_day
        package_id = self.params[0]
        package = self.app_data.get_package_by_id(package_id)
        assigned_route = package.package_assigned_route
        if assigned_route:
            total_travel_time = assigned_route.total_distance()  # Assuming total_distance returns the total travel time in hours
            if day_today > assigned_route.set_off_time:
                package.status = PackageStatus.EN_ROUTE
            if day_today > assigned_route.set_off_time + timedelta(hours=total_travel_time):
                package.status = PackageStatus.DELIVERED
            return f"The package is {package.status.value}"
        else:
            package.status = PackageStatus.NOT_ASSIGNED
            return "The package is not assigned yet"