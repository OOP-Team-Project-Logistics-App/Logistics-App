from datetime import timedelta
from commands.validators.validation_helpers import try_parse_float
from core.application_data import ApplicationData
from models.constants.package_status import PackageStatus
from models.constants.truck_status import TruckStatus


class UpdateCurrentDayCommand:
    def __init__(self, params: list, app_data: ApplicationData):
        self.add_days = try_parse_float(params[0])
        self.app_data = app_data

    def execute(self):
        self.update_truck_status()
        self.remove_delivered_packages()
        return self.app_data.update_current_day(self.add_days)

    #Iterate through all routes, if the current day is bigger than the arrival time of the last location for each route
    #change the status of the truck that was assigned to that route to available
    def update_truck_status(self):
        for route in self.app_data._delivery_routes:
            if route.check_if_route_completed(self.app_data.current_day + timedelta(days = self.add_days)):
                truck = route._assigned_truck
                if truck:
                    truck._status = TruckStatus.AVAILABLE

    def remove_delivered_packages(self):
        for route in self.app_data._delivery_routes:
            for package in list(route.packages): #Creates a copy of the list with packages assigned to a certain route
                package.update_package_status(self.app_data.current_day + timedelta(days = self.add_days))
                if package.status == PackageStatus.DELIVERED:
                    route.remove_package(package)