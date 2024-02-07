from models.route import Route
from models.package import Package
from models.truck import Truck


class ApplicationData:
    def __init__(self):
        self._delivery_routes: list[Route] = []
        self._delivery_packages: list[Package] = []
        self._trucks: list[Truck] = []

    @property
    def delivery_routes(self):
        return tuple(self._delivery_routes)

    @property
    def delivery_packages(self):
        return tuple(self._delivery_packages)
    
    @property
    def trucks(self):
        return tuple(self._trucks)

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
        for idx, truck in enumerate(self._trucks):
            if truck.max_range >= route.total_distance() and truck.capacity >= route.total_weight():
                route.assign_truck(truck)
                self._trucks.pop(idx)
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

    def assign_package_to_route(self, package, route, start_location, end_location, weight, contact_info):
        package = Package(start_location, end_location, weight, contact_info)
        if package._start_location in route.locations and package._end_location in route.locations:
            route.add_package(package)
        raise ValueError("Package's start and end location do not fit the route.")