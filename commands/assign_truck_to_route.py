from commands.base.base_command import BaseCommand
from commands.validators.validation_helpers import try_parse_int
from core.application_data import ApplicationData


class AssignTruckToRouteCommand(BaseCommand):
    def __init__(self, params: list, app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        self.route_id = try_parse_int(self.params[0])
        route = self.app_data.get_route_by_id(self.route_id)
        if route.assigned_truck:
            raise ValueError("There is already a truck assigned to that route.")
        truck = self.app_data.find_suitable_truck(route)
        #If a suitable truck is found, assign a time period during which the truck is busy
        if truck:
            truck.assign(time_period = (route.set_off_time, route.arrival_time))
            
        return f"Truck with id {truck.id} was assigned to route id {route.id}."