from core.application_data import ApplicationData
from models.package import Package


class SearchRouteCommand:
    def __init__(self, package_ids: list, app_data: ApplicationData):
        self.package_ids = package_ids
        self.app_data = app_data

    def execute(self):
        found_routes = []
        for package_id in self.package_ids:
            package = self.app_data.get_package_by_id(package_id)
            try:
                routes = self.app_data.search_route(package.start_location, package.end_location)
                if not routes:
                    raise ValueError("No route found for the given start and end locations.")
                found_routes.extend(f"Route found for package {package.id}: {route.route_info()}" for route in routes)
            except ValueError as e:
                found_routes.append(str(e))
                
        return "\n".join(found_routes)