from commands.create_delivery_route import CreateDeliveryRouteCommand
from commands.create_delivery_package import CreateDeliveryPackageCommand
from commands.initialize_trucks import InitializeTrucksCommand
from commands.search_route import SearchRouteCommand
from commands.view_information import ViewInformationCommand
from commands.view_route import ViewRouteCommand
from commands.update_route import UpdateRouteCommand
from errors.invalid_command import InvalidCommand


class CommandFactory:
    def __init__(self, data):
        self._app_data = data

    def create(self, input_line):
        cmd, *params = input_line.split()

        if cmd.lower() == "createdeliveryroute":
            return CreateDeliveryRouteCommand(params, self._app_data)
        if cmd.lower() == "createdeliverypackage":
            return CreateDeliveryPackageCommand(params, self._app_data)
        if cmd.lower() == "searchroute":
            return SearchRouteCommand(params, self._app_data)
        if cmd.lower() == "viewinformation":
            return ViewInformationCommand(params, self._app_data)
        if cmd.lower() == "viewroute":
            return ViewRouteCommand(params, self._app_data)
        if cmd.lower() == "createtrucks":
            return InitializeTrucksCommand(self._app_data)
        if cmd.lower() == "updateroute":
            return UpdateRouteCommand(self._app_data)

        raise InvalidCommand(cmd)