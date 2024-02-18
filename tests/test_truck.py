from datetime import datetime, timedelta
import unittest
from core.application_data import ApplicationData
from commands.initialize_trucks import InitializeTrucksCommand
from models.route import Route
from models.package import Package
from models.constants.truck_status import TruckStatus

app_data = ApplicationData()
InitializeTrucksCommand(app_data).execute()

set_off = datetime.now()
locations = {"Brisbane": set_off + timedelta(hours=1), "Melbourne": set_off + timedelta(hours= 10)}
route1 = Route(set_off, locations)
package1 = Package("Brisbane", "Melbourne", 10000, "test1@testing.com")
package2 = Package("Brisbane", "Melbourne", 33000, "test2@testing.com")

class TruckShould(unittest.TestCase):
    app_data = ApplicationData()
    trucks = app_data.initialize_trucks()
    view_trucks = app_data._trucks
    truck1 = view_trucks[0]
    truck2 = view_trucks[12]
    truck3 = view_trucks[39]
    def test_initializerReturnCorrectValues(self):
        self.assertEqual(1001, self.truck1.id)
        self.assertEqual("Scania", self.truck1.name)
        self.assertEqual(42000, self.truck1.capacity)
        self.assertEqual(8000, self.truck1.max_range)
        self.assertEqual(1013, self.truck2.id)
        self.assertEqual("Man", self.truck2.name)
        self.assertEqual(37000, self.truck2.capacity)
        self.assertEqual(10000, self.truck2.max_range)
        self.assertEqual(1040, self.truck3.id)
        self.assertEqual("Actros", self.truck3.name)
        self.assertEqual(26000, self.truck3.capacity)
        self.assertEqual(13000, self.truck3.max_range)

    def test_assign_changesStatusAssignedTimePeriodsAndCapacity(self):
        self.assertEqual(self.truck1.status, TruckStatus.AVAILABLE)
        self.assertEqual(self.truck1._assigned_time_periods, [])
        self.truck1.assign((route1.set_off_time, route1.arrival_time))
        self.assertEqual(self.truck1.status, TruckStatus.UNAVAILABLE)
        self.assertEqual(self.truck1.assigned_time_periods[0], (route1.set_off_time, route1.arrival_time))

    def test_add_remove_package_weightChangesAttrOrRaisesError(self):
        self.assertEqual(42000, self.truck1.remaining_capacity)
        self.truck1.add_package_weight(package1)
        self.assertEqual(32000, self.truck1.remaining_capacity)

        with self.assertRaises(ValueError):
            self.truck1.add_package_weight(package2)

        self.truck1.remove_package_weight(package1)
        self.assertEqual(42000, self.truck1.remaining_capacity)

        self.truck1.add_package_weight(package2)
        self.assertEqual(9000, self.truck1.remaining_capacity)

    def test_strReturnCorrectTruckFormat(self):
        expected = "ID: 1040, Model: Actros, Capacity: 26000kg, Max range: 13000km"
        self.assertEqual(expected, str(self.truck3))










