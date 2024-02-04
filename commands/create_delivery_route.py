from datetime import datetime
from models.constants.distances import Distance
from core.application_data import ApplicationData
from models.route import Route


class CreateDeliveryRouteCommand:
    def __init__(self, params, app_data: ApplicationData):
        self.params = params
        self.app_data = app_data

    def execute(self):
        route_id = Route.id_counter()
        new_route = Route(route_id, self.params[0])
        for location in self.params[1:]:
            new_route.add_location(location)
        self.app_data.add_route(new_route)
        
        return new_route.route_info()