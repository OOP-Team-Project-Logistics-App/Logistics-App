import unittest
from datetime import datetime, timedelta
from models.route import Route


class Route_Should(unittest.TestCase):

    def setUp(self):
        self.set_off_time = datetime.now()
        self.locations = {"Brisbane": 500, "Sydney": 1000}
        self.route = Route(self.set_off_time, self.locations)

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

    