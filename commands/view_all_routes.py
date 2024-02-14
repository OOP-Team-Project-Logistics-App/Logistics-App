from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData


class ViewInProgressRoutesCommand(BaseCommand):
    def __init__(self, params: list, app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        routes = self.app_data._delivery_routes
        current_time = self.app_data.current_day

        output_string = "Information about in-progress routes:"
        for route in routes:
            truck = route.assigned_truck
            packages = route.packages
            if route.set_off_time <= current_time < route.arrival_time:
                output_string += f"\n{route.route_info()}"
                output_string += f"\nTruck {str(truck)}"
                output_string += "\nPackages:"
                if packages:
                    output_string += "\n" + "\n".join(str(package.package_info()) for package in packages)
                else:
                    output_string += "\nNo packages assigned to this route."
        
        return output_string