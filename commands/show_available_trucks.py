from core.application_data import ApplicationData
from commands.validators.validation_helpers import validate_login


class ShowAvailableTrucks:
    def __init__(self, app_data: ApplicationData):
        self._app_data = app_data

    def execute(self):
        validate_login(self._app_data, requires_login = True)
        return self._app_data.show_available_trucks()