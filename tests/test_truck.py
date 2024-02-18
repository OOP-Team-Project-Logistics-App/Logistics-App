from datetime import datetime, timedelta
import unittest
from core.application_data import ApplicationData
from models.route import Route
from models.package import Package
from models.constants.truck_status import TruckStatus


class Truck_Should(unittest.TestCase):

    def setUp(self):
        app_data = ApplicationData()
        app_data.initialize_trucks()
        self.truck_1 = app_data.trucks[0]
        self.truck_2 = app_data.trucks[10]
        self.truck_3 = app_data.trucks[25]
        set_off_time = datetime.now()
        locations = {"Brisbane": set_off_time + timedelta(hours = 1), "Melbourne": set_off_time + timedelta(hours = 10)}
        self.route = Route(set_off_time, locations)
        self.package_1 = Package("Brisbane", "Melbourne", 10000, "test1@test.com")
        self.package_2 = Package("Brisbane", "Melbourne", 33000, "test2@test.com")

    def test_initializer_whenReturnsCorrectValues(self):
        self.assertEqual(1001, self.truck_1.id)
        self.assertEqual("Scania", self.truck_1.name)
        self.assertEqual(42000, self.truck_1.capacity)
        self.assertEqual(8000, self.truck_1.max_range)

        self.assertEqual(1011, self.truck_2.id)
        self.assertEqual("Man", self.truck_2.name)
        self.assertEqual(37000, self.truck_2.capacity)
        self.assertEqual(10000, self.truck_2.max_range)

        self.assertEqual(1026, self.truck_3.id)
        self.assertEqual("Actros", self.truck_3.name)
        self.assertEqual(26000, self.truck_3.capacity)
        self.assertEqual(13000, self.truck_3.max_range)

    def test_assigned_time_periods_whenReturnsTuple(self):
        self.assertIsInstance(self.truck_1.assigned_time_periods, tuple)

    def test_assign_whenAssignedTimePeriodsChangesStatusAndCapacity(self):
        self.assertEqual(self.truck_1.status, TruckStatus.AVAILABLE)
        self.assertEqual(self.truck_1._assigned_time_periods, [])
        self.truck_1.assign((self.route.set_off_time, self.route.arrival_time))
        self.assertEqual(self.truck_1.status, TruckStatus.UNAVAILABLE)
        self.assertEqual(self.truck_1.assigned_time_periods[0], (self.route.set_off_time, self.route.arrival_time))

    def test_add_remove_package_whenWeightChangesValueOrRaisesError(self):
        self.assertEqual(42000, self.truck_1.remaining_capacity)
        self.truck_1.add_package_weight(self.package_1)
        self.assertEqual(32000, self.truck_1.remaining_capacity)

        with self.assertRaises(ValueError):
            self.truck_1.add_package_weight(self.package_2)

        self.truck_1.remove_package_weight(self.package_1)
        self.assertEqual(42000, self.truck_1.remaining_capacity)

        self.truck_1.add_package_weight(self.package_2)
        self.assertEqual(9000, self.truck_1.remaining_capacity)

    def test_str_returnCorrectlyFormattedString(self):
        expected_output = "ID: 1026, Model: Actros, Capacity: 26000kg, Max range: 13000km"
        self.assertEqual(expected_output, str(self.truck_3))