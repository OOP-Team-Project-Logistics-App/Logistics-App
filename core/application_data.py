from datetime import datetime, timedelta
from models.constants.date_and_time_data import format_date
from models.route import Route
from models.package import Package
from models.truck import Truck


class ApplicationData:
    def __init__(self):
        self._delivery_routes: list[Route] = []
        self._delivery_packages: list[Package] = []
        self._trucks: list[Truck] = []
        self._current_day = datetime.now()

    @property
    def delivery_routes(self):
        return tuple(self._delivery_routes)

    @property
    def delivery_packages(self):
        return tuple(self._delivery_packages)
    
    @property
    def trucks(self):
        return tuple(self._trucks)
    
    @property
    def current_day(self):
        return self._current_day

    def add_route(self, route: Route):
        self._delivery_routes.append(route)

    def add_package(self, package: Package):
        if package not in self._delivery_packages:
            self._delivery_packages.append(package)

    def initialize_trucks(self):
        self._trucks.extend([Truck(id, "Scania", 42000, 8000) for id in range(1001, 1011)])
        self._trucks.extend([Truck(id, "Man", 37000, 10000) for id in range(1011, 1026)])
        self._trucks.extend([Truck(id, "Actros", 26000, 13000) for id in range(1026, 1041)])

    def find_suitable_truck(self, route: Route):
        for truck in self._trucks:
            if truck.max_range >= route.total_distance() and truck.capacity >= route.total_weight():
                if truck.assigned_time_period is None or truck.assigned_time_period[1] <= route.set_off_time or \
                        route.calculate_arrival_time() <= truck.assigned_time_period[0]:
                    route.assign_truck(truck)
                    return truck
        raise ValueError("There is no suitable truck for this route.")

    def get_route_by_id(self, route_id: int):
        for route in self._delivery_routes:
            if route.id == int(route_id):
                return route
        raise ValueError("Route with this id was not found.")
    
    def get_package_by_id(self, package_id: int):
        for package in self._delivery_packages:
            if package.id == int(package_id):
                return package
        raise ValueError("Package with this id was not found.")
    
    def get_truck_by_id(self, truck_id):
        for truck in self._trucks:
            if truck.id == truck_id:
                return truck
        raise ValueError("Truck with this id was not found.")
    
    def search_route(self, start_location: str, end_location: str):
        matching_routes = [route for route in self._delivery_routes 
                            if start_location in route.locations and end_location in route.locations
                            and route.locations.index(start_location) < route.locations.index(end_location)]
        return matching_routes

    def assign_package_to_route(self, package, route, start_location, end_location, weight, contact_info):
        package = Package(start_location, end_location, weight, contact_info)
        if package._start_location in route.locations and package._end_location in route.locations:
            route.add_package(package)
        raise ValueError("Package's start and end location do not fit the route.")
    
    def view_unassigned_packages(self):
        unassigned_packages = [package for package in self.delivery_packages if package._package_assigned_route is None]
        formatted_packages = [f"Package ID: {package.id}\n"
                            f"Start Location: {package.start_location}\n"
                            f"End Location: {package.end_location}" for package in unassigned_packages]
        return "\n".join(formatted_packages)
    
    def update_current_day(self, add_days):
        if add_days < 0:
            raise ValueError("Cannot set a date in the past, you can only add days.")
        self._current_day += timedelta(days = add_days)
        return f"Current day is now {format_date(self.current_day)}."