from core.application_data import ApplicationData
from models.package import Package


class AssignPackageToRouteCommand:
    def __init__(self, params, app_data: ApplicationData):
        self.params = params
        self.app_data = app_data

    def execute(self):
        package_id, route_id = self.params
        package = self.app_data.get_package_by_id(package_id)
        route = self.app_data.get_route_by_id(route_id)
        assigned_truck = route.assigned_truck

        if assigned_truck is None:
            raise ValueError("Selected route has no assigned truck.")
        if package.weight > assigned_truck.capacity - route.total_weight():
            raise ValueError("Package weight exceeds assigned truck's remaining capacity.")
        route.add_package(package)

        return f"Package with id {package_id} was assigned to route {route_id}."