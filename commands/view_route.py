from core.application_data import ApplicationData


class ViewRouteCommand:
    def __init__(self, params, app_data):
        self.route_id = params[0]
        self.app_data = app_data

    def execute(self):
        route = self.app_data.get_route_by_id(self.route_id)
        truck = route.assigned_truck
        packages = route.packages

        output_string = f"Information about Route {route.id}: \n"
        output_string += f"{route.route_info()} \n"
        output_string += f"Truck {str(truck)} \n"
        output_string += "Packages:\n"
        output_string += "\n".join(str(package.package_info()) for package in packages)
        
        return output_string