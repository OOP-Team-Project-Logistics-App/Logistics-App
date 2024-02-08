from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData


class SearchRouteCommand(BaseCommand):
    def __init__(self, params: list, app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        found_routes = []
        for package_id in self.params:
            package = self.app_data.get_package_by_id(package_id)
            try:
                routes = self.app_data.search_route(package.start_location, package.end_location)
                if not routes:
                    raise ValueError("No route found for the given start and end locations.")
                found_routes.extend(f"Route found for package {package.id}: {route.route_info()}" for route in routes)
            except ValueError as e:
                found_routes.append(str(e))
                
        return "\n".join(found_routes)