from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from commands.validators.validation_helpers import validate_login


class LoginCommand(BaseCommand):
    def __init__(self, params: list, app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        validate_login(self._app_data, requires_login=False)  # Validate login

        self._throw_if_user_logged_in()

        username = self.params[0]
        password = self.params[1]
        user = self._app_data.find_user_by_username(username)
        if user.password != password:
            raise ValueError('Wrong username or password!')
        else:
            self._app_data.login(user)

            return f'User {user.username} successfully logged in!'

    def _throw_if_user_logged_in(self):
        if self._app_data.has_logged_in_user:
            logged_user = self._app_data.logged_in_user
            raise ValueError(
                f'User {logged_user.username} is logged in! Please log out first!')
