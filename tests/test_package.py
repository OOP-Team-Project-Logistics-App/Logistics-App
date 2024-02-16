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