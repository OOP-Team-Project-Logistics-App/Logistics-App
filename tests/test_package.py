from datetime import datetime, timedelta
import unittest
from models.constants.package_status import PackageStatus
from models.package import Package
from models.route import Route


class Package_Should(unittest.TestCase):

    def setUp(self):
        Package.id_count = 0
        self.start_location = "Brisbane"
        self.end_location = "Sydney"
        self.weight = 5000
        self.contact_info = "test@test.com"
        self.package = Package(self.start_location, self.end_location, self.weight, self.contact_info)

    def test_initializator_whenParamsAreValid(self):
        self.assertEqual(self.package.id, 1)
        self.assertEqual(self.package.start_location, self.start_location)
        self.assertEqual(self.package.end_location, self.end_location)
        self.assertEqual(self.package.weight, self.weight)
        self.assertEqual(self.package.contact_info, self.contact_info)
        self.assertIsNone(self.package.package_assigned_route)
        self.assertEqual(self.package.status, PackageStatus.NOT_ASSIGNED)

    def test_package_idcounter_whenIsValid(self):
        Package.id_count = 0
        package_1 = Package("Brisbane", "Sydney", 5000, "test1@test.com")
        self.assertEqual(package_1.id, 1)
        package_2 = Package("Brisbane", "Sydney", 5000, "test2@test.com")
        self.assertEqual(package_2.id, 2)
        self.assertNotEqual(package_1.id, package_2.id)

    def test_start_location_whenStartLocationIsInvalid(self):
        with self.assertRaises(ValueError):
            self.package.start_location = "TestCity"

    def test_end_location_whenEndLocationIsInvalid(self):
        with self.assertRaises(ValueError):
            self.package.end_location = self.start_location

    def test_initializator_whenWeightIsNegative(self):
        with self.assertRaises(ValueError):
            self.package = Package(self.start_location, self.end_location, -500, self.contact_info)

    def test_contact_info_whenContactInfoIsInvalid(self):
        with self.assertRaises(ValueError):
            self.package.contact_info = "testemail"

    def test_update_package_status_whenRouteAssignedOrNotAssigned(self):
        self.package.update_package_status(datetime.now())
        self.assertEqual(self.package.status, PackageStatus.NOT_ASSIGNED)
        set_off_time = datetime.now()
        locations = {self.start_location: set_off_time - timedelta(hours = 5),
                    self.end_location: set_off_time + timedelta(hours = 5)}
        route = Route(set_off_time, locations)
        self.package.package_assigned_route = route
        self.package.update_package_status(datetime.now())
        self.assertEqual(self.package.status, PackageStatus.EN_ROUTE)

    def test_update_package_status_whenNotADatetimeObject(self):
        with self.assertRaises(ValueError):
            self.package.update_package_status("Not a datetime object")