from models.route import Route
from models.package import Package


class ApplicationData:
    def __init__(self):
        self._delivery_routes: list[Route] = []
        self._delivery_packages: list[Package] = []

    def add_route(self, route):
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