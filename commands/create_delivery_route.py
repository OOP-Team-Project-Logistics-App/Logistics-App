from datetime import datetime
from models.constants.distances import Distance
from core.application_data import ApplicationData
from models.route import Route

class CreateDeliveryRouteCommand:
    def __init__(self, params, app_data: ApplicationData):
        self.params = params
        self.app_data = app_data

    def execute(self):
        new_route = Route(self.params[0], self.params[1])
        start_time = "6"
        for location in self.params[1:]:
            new_route.add_location(location)
        self.app_data.add_route(new_route)
        truck = self.app_data.find_suitable_truck(new_route)
        new_route.assign_truck(truck)
        return f"Route {' -> '.join(self.params)} created and truck with id {truck.id} is assigned"