from core.application_data import ApplicationData
from models.route import Route


class CreateDeliveryRouteCommand:
    def __init__(self, params, app_data):
        self.locations = params
        self.app_data = app_data

    def execute(self):
        new_route = Route(self.locations)
        self.app_data.add_route(new_route)

        return str(new_route)