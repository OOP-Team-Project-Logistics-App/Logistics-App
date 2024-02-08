from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from models.route import Route


class CreateDeliveryRouteCommand(BaseCommand):
    def __init__(self, params: list, app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        new_route = Route(self.params)
        self.app_data.add_route(new_route)

        return str(new_route)