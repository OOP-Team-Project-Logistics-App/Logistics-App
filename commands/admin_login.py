from core.application_data import ApplicationData

class AdminLoginLogoutCommand:
    def __init__(self, params, app_data: ApplicationData):
        self.params = params
        self.app_data = app_data

    def execute(self):
        pass