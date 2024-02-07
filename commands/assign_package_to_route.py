from core.application_data import ApplicationData
from models.package import Package

class AssignPackageToRouteCommand:
    def __init__(self, params, app_data: ApplicationData):
        self.params = params
        self.app_data = app_data

    def execute(self):
        package_id, route_id = self.params
        package = self.app_data.get_package_by_id(int(package_id))
        route = self.app_data.get_route_by_id(int(route_id))
        assigned_truck = route.assigned_truck
        print(assigned_truck.capacity)
        print(route.total_weight())
        if assigned_truck == None:
            raise ValueError("Selected route has no assigned truck")
        if package.weight > assigned_truck.capacity - route.total_weight():
            raise ValueError("Package weight exceeds assigned truck's remaining capacity")
        route.add_package(package)
        print(route.packages[0].weight)
        print(route.total_weight())


        return f"Package with id  was assigned to route id "