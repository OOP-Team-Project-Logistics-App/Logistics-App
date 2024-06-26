from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from commands.validators.validation_helpers import validate_login


class AssignPackageToRouteCommand(BaseCommand):
    def __init__(self, params: list, app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        validate_login(self.app_data, requires_login = True)
        package_id, route_id = self.params
        package = self.app_data.get_package_by_id(package_id)
        package_start_location = package.start_location
        package_end_location = package.end_location
        route = self.app_data.get_route_by_id(route_id)
        route_locations = list(route.locations.keys())
        assigned_truck = route.assigned_truck
        #Check if the route has an assigned truck
        if assigned_truck is None:
            raise ValueError(f"Route {route_id} has no assigned truck")
        #Check if the package weight doesn't exceed the truck's capacity minus the assigned packages to that route
        if package.weight > assigned_truck.remaining_capacity:
            raise ValueError("Package weight exceeds assigned truck's remaining capacity.")

        #Iterate through route locations to find a match for package start location,
        #then search for package end location within the remaining route locations.
        #If found, assign the package to the route and update relevant package and route data.
        for location in route_locations:
            if package_start_location == location:
                for location in route_locations[(route_locations.index(package_start_location)):]:
                    if location == package_end_location:
                        route.add_package(package)
                        package.package_assigned_route = route
                        assigned_truck.add_package_weight(package)
                        return f"Package with id {package_id} was assigned to route {route_id}."

        raise ValueError(f"This route has no locations in the direction of {package_start_location} to {package_end_location}")