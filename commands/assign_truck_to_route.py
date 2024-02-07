from models.route import Route
from core.application_data import ApplicationData

class AssignTruckToRouteCommand:
    def __init__(self, params, app_data: ApplicationData):
        self.route_id = int(params[0])
        self.app_data = app_data

    def execute(self):
        route = self.app_data.get_route_by_id(self.route_id)
        truck = self.app_data.find_suitable_truck(route)

        return f"Truck with id {truck.id} was assigned to route id {route.id}."