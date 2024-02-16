from core.application_data import ApplicationData


class InitializeEmployeesCommand:
    def __init__(self, app_data: ApplicationData):
        self.app_data = app_data

    def execute(self):
        self.app_data.initialize_employees()