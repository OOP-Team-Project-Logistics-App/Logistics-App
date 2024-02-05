from models.route import Route
from models.package import Package
from models.truck import Truck


class ApplicationData:
    def __init__(self):
        self._delivery_routes = []
        self._trucks = []

    def add_route(self, route_id, route):
        self._delivery_routes.append((route_id, route))

    def initialize_trucks(self):
        for id in range(1001, 1011):
            self._trucks.append(Truck(id, "Scania", 42000, 8000))
        for id in range(1011, 1026):
            self._trucks.append(Truck(id, "Man", 37000, 10000))
        for id in range(1026, 1041):
            self._trucks.append(Truck(id, "Actros", 26000, 13000))

    def find_suitable_truck(self, route):
        for idx, truck in enumerate(self._trucks):
            if truck.max_range >= route.total_distance():
                return self._trucks.pop(idx)
        raise ValueError("There is no suitable truck for this route.")

    def get_route(self, route_id):
        for id, route in self._delivery_routes:
            if id == route_id:
                return route
        raise ValueError(f"Route with this id was not found.")

    def assign_package_to_route(self, package: Package, route: Route):
        pass

    def route_info(self, route_id):
        pass

    def package_info(self, package_id):
        pass