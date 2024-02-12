from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from models.route import Route
from datetime import datetime, timedelta


class CreateDeliveryRouteCommand(BaseCommand):
    def __init__(self, params: list, app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        date_today = datetime.now()
        set_off = self.params[0]
        set_off_time = datetime.strptime(f"2024-{set_off}", "%Y-%m/%d/%H")
        if date_today > set_off_time:
            raise ValueError("Set off time cannot be in the past")
        if date_today + timedelta(days = 30) < set_off_time:
            raise ValueError("Set off time cannot be more than 30 days in the future")
        
        locations = self.params[1:]
        new_route = Route(set_off_time, locations)
        self.app_data.add_route(new_route)

        return str(new_route)