from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from models.route import Route


class CreateDeliveryRouteCommand(BaseCommand):
    def __init__(self, params: list, app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        set_off_time = self.params[0]
        locations = self.params[1:]
        new_route = Route(set_off_time, locations)
        self.app_data.add_route(new_route)

        return str(new_route)