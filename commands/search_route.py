from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from commands.validators.validation_helpers import validate_login


class SearchRouteCommand(BaseCommand):
    def __init__(self, params, app_data: ApplicationData):
        super().__init__(params, app_data)

    #Search for suitable routes when given the id of a package
    def execute(self):
        validate_login(self.app_data, requires_login = True)
        package_id = self._params[0]
        package = self.app_data.get_package_by_id(package_id)
        found_routes = [f"Route found for package {package.id}:"]
        try:
            routes = self.app_data.search_route(package.start_location, package.end_location)
            if not routes:
                raise ValueError("No route found for the given start and end locations.")
            found_routes.extend(f"{route.route_info()}" for route in routes)
        except ValueError as e:
            found_routes.append(str(e))
                
        return "\n".join(found_routes)