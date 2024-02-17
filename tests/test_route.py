import unittest
from datetime import datetime, timedelta
from models.constants.distance_data import Distance
from models.package import Package
from models.route import Route
from models.truck import Truck


class Route_Should(unittest.TestCase):

    def setUp(self):
        self.set_off_time = datetime.now()
        self.locations = {"Brisbane": 500, "Sydney": 1000}
        self.route = Route(self.set_off_time, self.locations)
        self.package_1 = Package("Brisbane", "Sydney", 500, "test@email.com")
        self.package_2 = Package("Sydney", "Melbourne", 500, "test_1@email.com")
        self.truck = Truck(1001, "Scania", 42000, 8000)

    def test_route_id_counter_whenIsValid(self):
        Route.id_count = 0
        new_route_1 = Route(self.set_off_time, self.locations)
        self.assertEqual(new_route_1.id, 1)
        new_route_2 = Route(self.set_off_time, self.locations)
        self.assertEqual(new_route_2.id, 2)

    def test_initializer_whenLocationsDictIsValid(self):
        self.assertDictEqual(self.route.locations, self.locations)

    def test_initializer_whenPackagesIsTuple(self):
        self.assertIsInstance(self.route.packages, tuple)
        self.assertEqual(len(self.route.packages), 0)

    def test_initializer_whenAssignedTruckIsNone(self):
        self.assertIsNone(self.route.assigned_truck)

    def test_initializer_whenSetOffTimeIsValid(self):
        self.assertEqual(self.route.set_off_time, self.set_off_time)

    def test_initializer_whenArrivalTimeIsCorrect(self):
        self.assertEqual(self.route.arrival_time, self.set_off_time + timedelta(hours = self.route.total_distance() / 87))

    def test_add_package_whenSuccessfullyAddedToRoute(self):
        self.route.add_package(self.package_1)
        self.assertIn(self.package_1, self.route.packages)

    def test_remove_package_whenSuccessfullyRemovedFromRoute(self):
        self.route.add_package(self.package_1)
        self.route.assign_truck(self.truck)
        self.route.remove_package(self.package_1)
        self.assertNotIn(self.package_1, self.route.packages)

    def test_assign_truck_whenSuccessfullyAssignedToRoute(self):
        self.route.assign_truck(self.truck)
        self.assertEqual(self.route.assigned_truck, self.truck)

    def test_total_distance_whenDistanceOfRouteIsCorrect(self):
        self.route._locations = {"Brisbane": 1, "Sydney": 2, "Melbourne": 3}
        _ = {("Brisbane", "Sydney"): 909, ("Sydney", "Melbourne"): 877, ("Brisbane", "Melbourne"): 1786}
        self.assertEqual(self.route.total_distance(), 1786)

    def test_total_weight_whenWeightIsCorrectlyCalculated(self):
        self.route.add_package(self.package_1)
        self.route.add_package(self.package_2)
        self.assertEqual(self.route.total_weight(), 1000)

    def test_check_if_route_completed_whenCompletionStatusIsCorrect(self):
        self.route._locations = {"Brisbane": 1, "Sydney": 2, "Melbourne": 3}
        self.assertFalse(self.route.check_if_route_completed(2))
        self.assertTrue(self.route.check_if_route_completed(4))