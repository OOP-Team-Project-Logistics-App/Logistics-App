from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from commands.validators.validation_helpers import validate_login


class LogoutCommand:
    def __init__(self, app_data: ApplicationData):
        self._app_data = app_data

    def execute(self):
        validate_login(self._app_data, requires_login = True)
        self._app_data.logout()

        return "User logged out."

