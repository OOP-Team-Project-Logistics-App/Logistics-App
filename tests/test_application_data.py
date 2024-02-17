import unittest
from core.application_data import ApplicationData


class ApplicationData_Should(unittest.TestCase):

    def setUp(self):
        self.app_data = ApplicationData()

    def test_initializer_whenDataTypesAreCorrect(self):
        self.assertIsInstance(self.app_data.delivery_routes, tuple)
        self.assertIsInstance(self.app_data.delivery_packages, tuple)
        self.assertIsInstance(self.app_data.trucks, tuple)
        self.assertIsInstance(self.app_data.employees, tuple)