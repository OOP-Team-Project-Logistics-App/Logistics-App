from models.route import Route
from models.package import Package
from models.truck import Truck
from models.scania import Scania
from models.man import Man
from models.actros import Actros


class ApplicationData:
    def __init__(self):
        self._delivery_routes: list[Route] = []
        self._delivery_packages: list[Package] = []

    def add_route(self, id, locations):
        route = Route(id, locations, start_time=0)
        self._delivery_routes.append(route)

    def add_package(self, package):
        self._delivery_packages.append(package)

    def find_suitable_route(self, route, package):
        pass

    def assign_package_to_route(self, package: Package, route: Route):
        pass

    def route_info(self, route_id):
        pass

    def package_info(self, package_id):
        pass

