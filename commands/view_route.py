from core.application_data import ApplicationData


class ViewRouteCommand:
    def __init__(self, params, app_data: ApplicationData):
        self.route_id = int(params[0])
        self.app_data = app_data

    def execute(self):
        for route in self.app_data._delivery_routes:
            if route.id == self.route_id:
                return route.route_info()
        raise ValueError(f"Route {self.route_id} could not be found.")