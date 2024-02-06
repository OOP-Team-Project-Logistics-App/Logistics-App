from models.route import Route
from core.application_data import ApplicationData

class UpdateRouteCommand:
    def __init__(self, params, app_data: ApplicationData):
        self.route_id = params[0]
        self.truck_id = params[1]
        self.app_data = app_data

    def execute(self):
        route_to_assign_to = self.app_data.get_route(self.route_id)
        self.app_data.show_available_trucks()