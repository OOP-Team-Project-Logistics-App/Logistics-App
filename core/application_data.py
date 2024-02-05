from models.route import Route
from models.package import Package
from models.truck import Truck
class ApplicationData:
    def __init__(self):
        self._delivery_routes: list[Route] = []
        self._delivery_packages: list[Package] = []
        self._trucks = []

    def add_route(self, route):
        self._delivery_routes.append(route)

    def add_package(self, package):
        self._delivery_packages.append(package)

    def find_suitable_truck(self, route):
        for id_truck in self._trucks:
            if 1011 <= id_truck <= 1025:
                truck_range = 10000
                route_range = route.total_distance_of_route()
                if truck_range >= route_range:
                    self._trucks.remove(id_truck)
                    return Truck(id_truck, "Man", 37000, 10000)
            elif 1001 <= id_truck <= 1010:
                truck_range = 8000
                if truck_range >= route.total_distance_of_route():
                    return Truck(id_truck, "Scania", 42000, 8000)
            elif 1026 <= id_truck <= 1041:
                truck_range = 13000
                if truck_range >= route.total_distance_of_route():
                    return Truck(id_truck, "Actros", 26000, 13000)

        raise ValueError("No suitable truck found for the route.")

    def find_suitable_route(self, route, package):
        pass

    def assign_package_to_route(self, package: Package, route: Route):
        pass

    def route_info(self, route_id):
        pass

    def package_info(self, package_id):
        pass