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

    def add_route(self, route_id: int, route: Route):
        self._delivery_routes.append((route_id, route))

    def initialize_trucks(self):
        for id in range(1001, 1010):
            self._trucks.append(Truck(id, "Scania", 42000, 8000))
        for id in range(1011, 1025):
            self._trucks.append(Truck(id, "Man", 37000, 10000))
        for id in range(1026, 1040):
            self._trucks.append(Truck(id, "Actros", 26000, 13000))

    def find_suitable_truck(self, route: Route):
        for idx, truck in enumerate(self._trucks):
            if truck.max_range >= route.total_distance():
                return self._trucks.pop(idx)
        raise ValueError("There is no suitable truck for this route.")

    def get_route(self, route_id: int):
        for id, route in self._delivery_routes:
            if id == route_id:
                return route
        raise ValueError("Route with this id was not found.")

    def assign_package_to_route(self, package: Package, route: Route):
        if package._start_location in route.locations and package._end_location in route.locations:
            route.add_package(package)
        raise ValueError("Package's start and end location do not fit the route.")

    def find_truck_by_id(self, truck_id):
        for truck in self._trucks:
            if truck.id == truck_id:
                return truck
        raise ValueError("Truck with this id was not found.")

    def show_available_trucks(self):
        trucks = {
            "Scania": {"id": range(1001, 1011), "max_range": 8000, "capacity": 42000},
            "Man": {"id": range(1011, 1026), "max_range": 10000, "capacity": 37000},
            "Actros": {"id": range(1026, 1041), "max_range": 13000, "capacity": 26000}
        }

        print("Available trucks:")
        for name, attributes in trucks.items():
            available_trucks = [truck for truck in self._trucks if truck.name == name]
            if available_trucks:
                ids = sorted(truck.id for truck in available_trucks)
                print(f"ID {ids[0]} to {ids[-1]}, {name}, {attributes['max_range']}km range, {attributes['capacity']}kg capacity")
            else:
                print(f"{name}, {attributes['range']}km range, {attributes['capacity']}kg capacity, None available")


    def route_info(self, route_id: int):
        pass

    def package_info(self, package_id: int):
        pass