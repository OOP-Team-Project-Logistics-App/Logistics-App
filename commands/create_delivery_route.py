from core.application_data import ApplicationData
from models.route import Route


class CreateDeliveryRouteCommand:
    def __init__(self, params, app_data):
        self.route_id = params[0]
        self.locations = params[1:]
        self.app_data = app_data

    def execute(self):
        new_route = Route(self.route_id, self.locations)
        truck = self.app_data.find_suitable_truck(new_route)
        new_route.assign_truck(truck)
        self.app_data.add_route(self.route_id, new_route)

        return str(new_route)