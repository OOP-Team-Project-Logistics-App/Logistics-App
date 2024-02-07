from core.application_data import ApplicationData


class ViewRouteCommand:
    def __init__(self, params, app_data):
        self.route_id = params[0]
        self.app_data = app_data

    def execute(self):
        route = self.app_data.get_route_by_id(self.route_id)
        truck = route.assigned_truck
        packages = route.packages

        return f"Information: {route}, \n \
            Truck: {str(truck)}, \n \
            Packages: {', '.join(str(package) for package in packages)}"