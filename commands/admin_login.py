from core.application_data import ApplicationData

class AdminLoginLogoutCommand:
    def __init__(self, params, app_data: ApplicationData):
        self.params = params
        self.app_data = app_data

    def execute(self):
        password_or_logout = self.params

        if password_or_logout.lower() == "logout":
            self.app_data.log_admin("logout")
        if password_or_logout == "password":
            self.app_data.log_admin("password")


