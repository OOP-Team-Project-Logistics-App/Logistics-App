from core.application_data import ApplicationData
from commands.update_current_day import UpdateCurrentDayCommand
from models.package import Package
from models.route import Route

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
            for location in assigned_route.locations: #Need arrival time for each city
                #if day_today >                       #Need break between cities
                pass
        else:
            return "The package is not assigned yet"