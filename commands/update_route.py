from models.route import Route
from core.application_data import ApplicationData

class UpdateRouteCommand:
    def __init__(self, app_data: ApplicationData):
        self.app_data = app_data

    def execute(self):
        self.app_data.show_available_trucks()
        route_to_assign_to = self.app_data.get_route(input("Enter route ID you wish to update: "))
        truck_id = input("Enter the truck ID you wish to assign: ")
        truck = self.app_data.find_suitable_truck(route_to_assign_to)
        truck = self.app_data.find_truck_by_id(truck_id)
        route_to_assign_to.assign_truck(truck)

        return f"Truck with id {truck_id} was assigned to {route_to_assign_to.id}."