from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from commands.validators.validation_helpers import validate_login


class LoginCommand(BaseCommand):
    def __init__(self, params: list, app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        validate_login(self._app_data, requires_login = False)
        self.user_already_logged_in() 

        username = self.params[0]
        password = self.params[1]
        user = self._app_data.find_user(username)
        if user.password != password:
            raise ValueError("Wrong password.")
        else:
            self._app_data.login(user)
            return f"{user.username} has logged in."

    def user_already_logged_in(self):
        if self._app_data.has_logged_in_user:
            logged_user = self._app_data.logged_in_user
            raise ValueError(f"{logged_user.username} is already logged in.")
