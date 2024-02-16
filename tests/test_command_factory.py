from datetime import datetime, timedelta
import unittest
from commands.create_delivery_package import CreateDeliveryPackageCommand
from commands.create_delivery_route import CreateDeliveryRouteCommand
from commands.update_current_day import UpdateCurrentDayCommand
from core.application_data import ApplicationData
from core.command_factory import CommandFactory
from errors.invalid_command import InvalidCommand


class CommandFactory_Should(unittest.TestCase):
    
    def setUp(self):
        self.app_data = ApplicationData()
        self.command_factory = CommandFactory(self.app_data)

        "createdeliveryroute", 
        "createdeliverypackage",
        "assigntrucktoroute",
        "assignpackagetoroute",
        "searchroute",
        "packagestatus",
        "getpackageinfo",
        "viewunassignedpackages",
        "viewroute",
        "viewallroutes"
        
    def test_command_createdeliveryroute_when_ValidParams(self):
        time = (datetime.now() + timedelta(days = 10)).strftime("%m/%d/%H")
        command = self.command_factory.create(f"createdeliveryroute {time} Brisbane Sydney")
        self.assertEqual(command.params[0], time)
        self.assertEqual(command.params[1:], ("Brisbane", "Sydney"))
        self.assertEqual(command.app_data, self.app_data)


    def test_command_createdeliveryroute_when_SetOffTimeInPast(self):
        time_in_past = (datetime.now() - timedelta(days=1)).strftime("%m/%d/%H")
        command = self.command_factory.create(f"createdeliveryroute {time_in_past} Brisbane Sydney Melbourne")
        with self.assertRaises(ValueError):
            command.execute()

    def test_command_createdeliveryroute_when_SetOffTimeTooFarInFuture(self):
        time_in_future = (datetime.now() + timedelta(days=31)).strftime("%m/%d/%H")
        command = self.command_factory.create(f"createdeliveryroute {time_in_future} Brisbane Sydney Melbourne")
        with self.assertRaises(ValueError):
            command.execute()

    def test_command_createdeliverypackage_whenValidParams(self):
        command = self.command_factory.create("createdeliverypackage Sydney Melbourne 100 test@email.com")
        self.assertIsNotNone(command)
        self.assertEqual(command._app_data, self.app_data)
        self.assertEqual(command._params, ["Sydney", "Melbourne", "100", "test@email.com"])
        self.assertIsInstance(command, CreateDeliveryPackageCommand)

    def test_command_updateday_whenValidParams(self):
        command = self.command_factory.create("updateday 1.0")
        self.assertIsNotNone(command)
        self.assertEqual(command._app_data, self.app_data)
        self.assertEqual(command._params, ["1.0"])
        self.assertIsInstance(command, UpdateCurrentDayCommand)

    def test_command_updateday_when_InvalidParams(self):
        with self.assertRaises(ValueError):
            self.command_factory.create("updateday param1")

    def test_command_showavailabletrucks_whenIsValid(self):
        command = self.command_factory.create("showavailabletrucks")
        self.assertIsNotNone(command)
        self.assertEqual(command._app_data, self.app_data)

    def test_commands_whenInvalidCommand(self):
        with self.assertRaises(InvalidCommand):
            self.command_factory.create("invalidcommand param1 param2")