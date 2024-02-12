from commands.create_delivery_route import CreateDeliveryRouteCommand
from commands.create_delivery_package import CreateDeliveryPackageCommand
from commands.get_package_info import GetPackageInformation
from commands.initialize_trucks import InitializeTrucksCommand
from commands.search_route import SearchRouteCommand
from commands.view_route import ViewRouteCommand
from commands.assign_truck_to_route import AssignTruckToRouteCommand
from commands.assign_package_to_route import AssignPackageToRouteCommand
from errors.invalid_command import InvalidCommand
from commands.update_current_day import UpdateCurrentDayCommand
from commands.package_status import PackageStatusCommand


class CommandFactory:
    def __init__(self, data):
        self._app_data = data

    def create(self, input_line):
        cmd, *params = input_line.split()

        if cmd.lower() == 'packagestatus':
            return PackageStatusCommand(params, self._app_data)
        if cmd.lower() == 'updateday':
            return UpdateCurrentDayCommand(params)
        if cmd.lower() == "createdeliveryroute":
            return CreateDeliveryRouteCommand(params, self._app_data)
        if cmd.lower() == "createdeliverypackage":
            return CreateDeliveryPackageCommand(params, self._app_data)
        if cmd.lower() == "searchroute":
            return SearchRouteCommand(params, self._app_data)
        if cmd.lower() == "viewroute":
            return ViewRouteCommand(params, self._app_data)
        if cmd.lower() == "createtrucks":
            return InitializeTrucksCommand(self._app_data)
        if cmd.lower() == "assigntrucktoroute":
            return AssignTruckToRouteCommand(params, self._app_data)
        if cmd.lower() == "assignpackagetoroute":
            return AssignPackageToRouteCommand(params, self._app_data)
        if cmd.lower() == "getpackageinfo":
            return GetPackageInformation(params, self._app_data)

        raise InvalidCommand(cmd)