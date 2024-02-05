from datetime import datetime
from core.application_data import ApplicationData


class AddLocationCommand:
    def __init__(self, params, app_data: ApplicationData):
        self.route_id = int(params[0])
        self.city = params[1]
        current_date = datetime.now().date()
        self.time = datetime(current_date.year, current_date.month, current_date.day, int(params[2]))
        self.app_data = app_data

    def execute(self):
        for route in self.app_data._delivery_routes:
            if route.id == self.route_id:
                route.add_location((self.city, self.time))
                formatted_time = self.time.strftime("%b %d %H:%M")
                return f"Location: {self.city} ({formatted_time}) added to route {self.route_id}."
        raise ValueError(f"Route {self.route_id} could not be found.")