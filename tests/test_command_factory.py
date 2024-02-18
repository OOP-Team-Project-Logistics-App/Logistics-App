from datetime import datetime, timedelta
import unittest
from commands.assign_package_to_route import AssignPackageToRouteCommand
from commands.assign_truck_to_route import AssignTruckToRouteCommand
from commands.create_delivery_package import CreateDeliveryPackageCommand
from commands.search_route import SearchRouteCommand
from commands.update_current_day import UpdateCurrentDayCommand
from core.application_data import ApplicationData
from core.command_factory import CommandFactory
from errors.invalid_command import InvalidCommand
from models.route import Route


class CommandFactory_Should(unittest.TestCase):
    
    def setUp(self):
        self.app_data = ApplicationData()
        self.command_factory = CommandFactory(self.app_data)
 
        "packagestatus",
        "getpackageinfo",
        "viewunassignedpackages",
        "viewroute",
        "viewallroutes"
        
    def test_command_createdeliveryroute_whenValidParams(self):
        time = (datetime.now() + timedelta(days = 10)).strftime("%m/%d/%H")
        command = self.command_factory.create(f"createdeliveryroute {time} Brisbane Sydney")
        self.assertEqual(command.params[0], time)
        self.assertEqual(command.params[1:], ("Brisbane", "Sydney"))
        self.assertEqual(command.app_data, self.app_data)

    def test_command_createdeliveryroute_whenSetOffTimeInPast(self):
        time_in_past = (datetime.now() - timedelta(days = 1)).strftime("%m/%d/%H")
        command = self.command_factory.create(f"createdeliveryroute {time_in_past} Brisbane Sydney Melbourne")
        with self.assertRaises(ValueError):
            command.execute()

    def test_command_createdeliveryroute_whenSetOffTimeTooFarInFuture(self):
        time_in_future = (datetime.now() + timedelta(days = 31)).strftime("%m/%d/%H")
        command = self.command_factory.create(f"createdeliveryroute {time_in_future} Brisbane Sydney Melbourne")
        with self.assertRaises(ValueError):
            command.execute()

    def test_command_createdeliverypackage_whenValidParams(self):
        command = self.command_factory.create("createdeliverypackage Sydney Melbourne 100 test@email.com")
        self.assertIsNotNone(command)
        self.assertEqual(command._app_data, self.app_data)
        self.assertEqual(command._params, ["Sydney", "Melbourne", "100", "test@email.com"])
        self.assertIsInstance(command, CreateDeliveryPackageCommand)

    def test_command_searchroute_whenValidParams(self):
        command = self.command_factory.create("searchroute 1")
        self.assertIsNotNone(command)
        self.assertEqual(command._app_data, self.app_data)
        self.assertEqual(command._params, ["1"])
        self.assertIsInstance(command, SearchRouteCommand)

    def test_command_assigntrucktoroute_whenValidParams(self):
        command = self.command_factory.create("assigntrucktoroute 1")
        self.assertIsNotNone(command)
        self.assertEqual(command._app_data, self.app_data)
        self.assertEqual(command._params, ["1"])
        self.assertIsInstance(command, AssignTruckToRouteCommand)

    def test_command_assigntrucktoroute_whenInvalidParams(self):
        command = self.command_factory.create("assigntrucktoroute invalidparam")
        with self.assertRaises(ValueError):
            command.execute()

    def test_command_assignpackagetoroute_whenValidParams(self):
        command = self.command_factory.create("assignpackagetoroute 1 1")
        self.assertIsNotNone(command)
        self.assertEqual(command._app_data, self.app_data)
        self.assertEqual(command._params, ["1", "1"])
        self.assertIsInstance(command, AssignPackageToRouteCommand)

    def test_command_assignpackagetoroute_whenInvalidParams(self):
        command = self.command_factory.create("assignpackagetoroute invalidparam")
        with self.assertRaises(ValueError):
            command.execute()

    def test_command_searchroute_whenInvalidParams(self):
        command = self.command_factory.create("searchroute invalidparam")
        with self.assertRaises(ValueError):
            command.execute()

    def test_command_updateday_whenValidParams(self):
        command = self.command_factory.create("updateday 1.0")
        self.assertIsNotNone(command)
        self.assertEqual(command._app_data, self.app_data)
        self.assertEqual(command._params, ["1.0"])
        self.assertIsInstance(command, UpdateCurrentDayCommand)

    def test_command_updateday_whenInvalidParams(self):
        with self.assertRaises(ValueError):
            self.command_factory.create("updateday param1")

    def test_command_showavailabletrucks_whenIsValid(self):
        command = self.command_factory.create("showavailabletrucks")
        self.assertIsNotNone(command)
        self.assertEqual(command._app_data, self.app_data)

    def test_commands_whenInvalidCommand(self):
        with self.assertRaises(InvalidCommand):
            self.command_factory.create("invalidcommand param1 param2")