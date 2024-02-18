from datetime import datetime, timedelta
import unittest
from core.application_data import ApplicationData
from models.constants.job_title import JobTitle
from models.constants.truck_status import TruckStatus
from models.package import Package
from models.route import Route
from models.truck import Truck
from models.user import User


class ApplicationData_Should(unittest.TestCase):

    def setUp(self):
        self.app_data = ApplicationData()
        self.set_off_time = datetime.now()
        self.locations = {"Brisbane": self.set_off_time + timedelta(hours = 1), "Sydney": self.set_off_time + timedelta(hours = 10)}
        self.route = Route(self.set_off_time, self.locations)
        self.start_location = "Brisbane"
        self.end_location = "Sydney"
        self.weight = 5000
        self.contact_info = "test@test.com"
        self.package = Package(self.start_location, self.end_location, self.weight, self.contact_info)
        self.user = User("Employee", "Epassword", JobTitle.EMPLOYEE)

    def test_initializer_whenDataTypesAreCorrect(self):
        self.assertIsInstance(self.app_data.delivery_routes, tuple)
        self.assertIsInstance(self.app_data.delivery_packages, tuple)
        self.assertIsInstance(self.app_data.trucks, tuple)
        self.assertIsInstance(self.app_data.employees, tuple)

    def test_add_route_whenAddsRouteProperly(self):
        self.app_data.add_route(self.route)
        self.assertIn(self.route, self.app_data.delivery_routes)

    def test_add_package_whenAddsPackageProperly(self):
        self.app_data.add_package(self.package)
        self.assertIn(self.package, self.app_data.delivery_packages)

    def test_initialize_trucks_whenInitializesCorrectAmount(self):
        self.app_data.initialize_trucks()
        self.assertEqual(len(self.app_data.trucks), 40)

    def test_initialize_employees_whenInitializesCorrectAmount(self):
        self.app_data.initialize_employees()
        self.assertEqual(len(self.app_data.employees), 3)

    def test_find_suitable_truck_whenCorrectlyAssignsTruck(self):
        self.app_data.initialize_trucks()
        truck = self.app_data.find_suitable_truck(self.route)
        self.assertIsInstance(truck, Truck)

    def test_find_user_whenRetrievesUserByUsername(self):
        self.app_data.initialize_employees()
        user = self.app_data.find_user("Employee")
        self.assertIsInstance(user, User)

    def test_get_route_by_id_whenRetrievesRouteById(self):
        self.app_data.add_route(self.route)
        route_return = self.app_data.get_route_by_id(self.route.id)
        self.assertEqual(route_return, self.route)

    def test_get_package_by_id_whenRetrievesPackageById(self):
        self.app_data.add_package(self.package)
        package_return = self.app_data.get_package_by_id(self.package.id)
        self.assertEqual(package_return, self.package)

    def test_search_route_whenSearchesForRouteSuccessfully(self):
        self.app_data.add_route(self.route)
        start_location, end_location = "Brisbane", "Sydney"
        matching_routes = self.app_data.search_route(start_location, end_location)
        self.assertIn(self.route, matching_routes)

    def test_view_unassigned_packages_whenViewsUnassignedPackagesSuccessfully(self):
        self.app_data.add_package(self.package)
        unassigned_packages_string = self.app_data.view_unassigned_packages()
        self.assertIsInstance(unassigned_packages_string, str)
        output_string = (f"Package ID: {self.package.id}\n"
                      f"Start Location: {self.package.start_location}\n"
                      f"End Location: {self.package.end_location}")
        self.assertIn(output_string, unassigned_packages_string)

    def test_update_current_day_whenUpdatesSuccessfully(self):
        current_day = self.app_data.current_day
        self.app_data.update_current_day(1)
        self.assertEqual(self.app_data.current_day, current_day + timedelta(days = 1))

    def test_show_available_trucks_returnsCorrectlyFormattedString(self):
        truck_return_string = self.app_data.show_available_trucks()
        for truck_name in ["Scania", "Man", "Actros"]:
            available_trucks = sum(1 for truck in self.app_data.trucks if truck.name == truck_name and truck.status == TruckStatus.AVAILABLE)
            total_trucks = sum(1 for truck in self.app_data.trucks if truck.name == truck_name)
            unavailable_trucks = total_trucks - available_trucks
            self.assertIn(f"-------\n"
                        f"{truck_name}:\n"
                        f"Available: {available_trucks} trucks, Unavailable: {unavailable_trucks} trucks", truck_return_string)
            
    def test_logged_in_user_raisesError_whenNoUserLogged(self):
        with self.assertRaises(ValueError):
            self.app_data.logged_in_user

    def test_has_logged_in_user_returnsUserLoggedInOrNot(self):
        self.assertFalse(self.app_data.has_logged_in_user)
        self.app_data._logged_user = self.user
        self.assertTrue(self.app_data.has_logged_in_user)

    def test_login_whenUserLogsSuccessfully(self):
        self.assertIsNone(self.app_data._logged_user)
        self.app_data.login(self.user)
        self.assertEqual(self.app_data._logged_user, self.user)

    def test_logout_whenUserLogoutsSuccessfully(self):
        self.app_data.login(self.user)
        self.assertEqual(self.app_data._logged_user, self.user)
        self.app_data.logout()
        self.assertIsNone(self.app_data._logged_user)