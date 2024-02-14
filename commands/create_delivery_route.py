from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from models.constants.date_and_time_data import calculate_travel_time
from models.route import Route
from datetime import datetime, timedelta


class CreateDeliveryRouteCommand(BaseCommand):
    def __init__(self, params: list, app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        date_today = self.app_data.current_day
        set_off = self.params[0]
        set_off_time = datetime.strptime(f"2024-{set_off}", "%Y-%m/%d/%H")
        if date_today > set_off_time:
            raise ValueError("Set off time cannot be in the past")
        if date_today + timedelta(days = 30) < set_off_time:
            raise ValueError("Set off time cannot be more than 30 days in the future")
        
        locations = self.params[1:]
        dict_locations = {location: set_off_time + calculate_travel_time(locations[0], location) for location in locations}
        new_route = self.app_data.add_route(Route(set_off_time, dict_locations))
        
        return str(new_route)