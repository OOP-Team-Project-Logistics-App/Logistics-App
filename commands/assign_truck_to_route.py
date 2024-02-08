from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData


class AssignTruckToRouteCommand(BaseCommand):
    def __init__(self, params: list, app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        self.route_id = int(self.params[0])
        route = self.app_data.get_route_by_id(self.route_id)
        truck = self.app_data.find_suitable_truck(route)

        return f"Truck with id {truck.id} was assigned to route id {route.id}."