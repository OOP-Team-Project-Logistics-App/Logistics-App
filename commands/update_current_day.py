from datetime import timedelta
from commands.validators.validation_helpers import try_parse_float
from core.application_data import ApplicationData
from models.constants.truck_status import TruckStatus


class UpdateCurrentDayCommand:
    def __init__(self, params: list, app_data: ApplicationData):
        self.add_days = try_parse_float(params[0])
        self.app_data = app_data

    def execute(self):
        self.update_truck_status()
        return self.app_data.update_current_day(self.add_days)
    #Iterate through all routes, if the current day is bigger than the arrival time of the last location for each route
    #change the status of the truck that was assigned to that route to available
    def update_truck_status(self):
        for route in self.app_data._delivery_routes:
            if route.check_if_route_completed(self.app_data.current_day + timedelta(days = self.add_days)):
                truck = route._assigned_truck
                if truck:
                    truck._status = TruckStatus.AVAILABLE