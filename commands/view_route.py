from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData


class ViewRouteCommand(BaseCommand):
    def __init__(self, params: list, app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        self.route_id = self.params[0]
        route = self.app_data.get_route_by_id(self.route_id)
        truck = route.assigned_truck
        packages = route.packages

        output_string = f"Information about Route {route.id}: \n"
        output_string += f"{route.route_info()} \n"
        output_string += f"Truck {str(truck)} \n"
        output_string += "Packages:\n"
        output_string += "\n".join(str(package.package_info()) for package in packages)
        
        return output_string