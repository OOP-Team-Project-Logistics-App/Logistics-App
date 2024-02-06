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
            if int(id) == route_id:
                return route
        raise ValueError(f"Route with this id was not found.")

    def assign_package_to_route(self, package: Package, route: Route):
        if package._start_location and package._end_location in route:
            route.add_package(package)
        raise ValueError("Package's start and end location do not fit the route.")

    def find_truck_by_id(self, truck_id):
        for truck in self._trucks:
            if truck.id == truck_id:
                return truck

    def show_available_trucks(self):
        print("Available trucks:")
        free_scania, free_man, free_actros = 0, 0, 0
        for truck in self._trucks:
            if truck.id <= 1010:
                free_scania += 1
            if truck.id > 1010 and truck.id <= 1025:
                free_man += 1
            if truck.id > 1025:
                free_actros +=1
        if free_scania == 0:
            print("model Scania, 8000km range, 42000kg capacity, None available")
        else:
            print(f"ID {1010 - free_scania} to 1010, model Scania, 8000km range, 42000kg capacity")
        if free_man == 0:
            print("model Scania, 10000km range, 37000kg capacity, None available")
        else:
            print(f"ID {1025 - free_man} to 1025, model Man, 10000km range, 37000kg capacity")
        if free_actros == 0:
            print("model Actros, 13000km range, 26000kg capacity, None available")
        else:
            print(f"ID {1040 - free_scania} to 1040, model Actros, 13000km range, 26000kg capacity")


    def route_info(self, route_id: int):
        pass

    def package_info(self, package_id: int):
        pass