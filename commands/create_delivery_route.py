from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from models.constants.date_and_time_data import calculate_travel_time
from models.route import Route
from datetime import datetime, timedelta
from commands.validators.validation_helpers import validate_login


class CreateDeliveryRouteCommand(BaseCommand):
    def __init__(self, params: list, app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        validate_login(self.app_data, requires_login = True)
        date_today = self.app_data.current_day
        set_off = self.params[0]
        set_off_time = datetime.strptime(f"2024-{set_off}", "%Y-%m/%d/%H")
        if date_today > set_off_time:
            raise ValueError("Set off time cannot be in the past.")
        if date_today + timedelta(days = 30) < set_off_time:
            raise ValueError("Set off time cannot be more than 30 days in the future.")
        
        #Calculates the arrival time for each location along the route, based on the set_off_time and the travel time
        #between consecutive locations, then creates a new route object with these calculated arrival times.
        locations = self.params[1:]
        dict_locations = {}
        start_location = locations[0]
        arrival_time = set_off_time
        for i in range(len(locations)):
            location = locations[i]
            arrival_time += calculate_travel_time(start_location, location)
            dict_locations[location] = arrival_time
            start_location = location
        new_route = Route(set_off_time, dict_locations)
        self.app_data.add_route(new_route)

        return str(new_route)