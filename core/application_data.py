import os
import pickle
from datetime import datetime, timedelta
from models.constants.date_and_time_data import format_date
from models.route import Route
from models.package import Package
from models.truck import Truck
from models.constants.truck_status import TruckStatus
from models.user import User
from models.constants.job_title import JobTitle


class ApplicationData:
    def __init__(self):
        self._delivery_routes: list[Route] = []
        self._delivery_packages: list[Package] = []
        self._trucks: list[Truck] = []
        self._employees: list[User] = []
        self._current_day = datetime.now()
        self._logged_user = None

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
    def employees(self):
        return tuple(self._employees)
    
    @property
    def current_day(self):
        return self._current_day
    
    @property
    def logged_in_user(self):
        if self.has_logged_in_user:
            return self._logged_user
        else:
            raise ValueError("There is no logged in user.")

    @property
    def has_logged_in_user(self):
        return self._logged_user is not None
    
    def save_system_state(self):
        data = {"Routes": self._delivery_routes,
                "Packages": self._delivery_packages,
                "Trucks": self._trucks,
                "Employees": self._employees}
 
        file_path = "data/app_data.pickle"
        if not os.path.exists(os.path.dirname(file_path)):
            os.mkdir(os.path.dirname(file_path))
 
        with open(file_path, "wb") as file:
            pickle.dump(data, file)
 
    def load_system_state(self):
        file_path = "data/app_data.pickle"
        if os.path.isfile(file_path):
            with open(file_path, "rb") as file:
                data = pickle.load(file)
                self._delivery_routes = data["Routes"]
                self._delivery_packages = data["Packages"]
                self._trucks = data["Trucks"]
                self._employees = data["Employees"]

    def add_route(self, route: Route):
        self._delivery_routes.append(route)

    def add_package(self, package: Package):
        self._delivery_packages.append(package)

    def initialize_trucks(self):
        self._trucks.extend([Truck(id, "Scania", 42000, 8000) for id in range(1001, 1011)])
        self._trucks.extend([Truck(id, "Man", 37000, 10000) for id in range(1011, 1026)])
        self._trucks.extend([Truck(id, "Actros", 26000, 13000) for id in range(1026, 1041)])

    def initialize_employees(self):
        self._employees.extend([User("Employee", "Epassword", JobTitle.EMPLOYEE)])
        self._employees.extend([User("Supervisor", "Spassword", JobTitle.SUPERVISOR)])
        self._employees.extend([User("Manager", "Mpassword", JobTitle.MANAGER)])

    #Iterate through each truck, if both the range and the capacity of the truck satisfy the demands for the completion
    #of the new route, check if the truck has any assigned routes. If any routes are assigned, check if the set off time
    #of the new route overlaps with the arrival time of each assigned route, and the arrival time of the new route
    #overlaps with the set off time of each assigned route. If conflict is found, do the same checks for the next truck.
    def find_suitable_truck(self, route: Route):
        for truck in self._trucks:
            if truck.max_range >= route.total_distance() and truck.capacity >= route.total_weight():
                time_conflict = False
                for time_period in truck._assigned_time_periods:
                    if not (route.set_off_time >= time_period[1] or route.arrival_time <= time_period[0]):
                        time_conflict = True
                        break
                if not time_conflict:
                    route.assign_truck(truck)
                    return truck
        raise ValueError("There is no suitable truck for this route.")
    
    def find_user(self, username: str):
        for user in self._employees:
            if user.username == username:
                return user
        raise ValueError("There is no user with that username.")

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
    
    def search_route(self, start_location: str, end_location: str):
        matching_routes = [route for route in self._delivery_routes 
                            if start_location in route.locations and end_location in route.locations
                            and tuple(route.locations).index(start_location) < tuple(route.locations).index(end_location)]
        return matching_routes
    
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
    
    def show_available_trucks(self):
        truck_names = ["Scania", "Man", "Actros"]
        result = []
        for truck_name in truck_names:
            total_trucks = sum(1 for truck in self._trucks if truck.name == truck_name)
            available_trucks = sum(1 for truck in self._trucks if truck.name == truck_name and truck.status == TruckStatus.AVAILABLE)
            unavailable_trucks = total_trucks - available_trucks
            result.append(f"-------\n"
                        f"{truck_name}:\n"
                        f"Available: {available_trucks} trucks, Unavailable: {unavailable_trucks} trucks")

        return "\n".join(result)
    
    def login(self, user: User):
        self._logged_user = user

    def logout(self):
        self._logged_user = None