from core.application_data import ApplicationData


class ShowAvailableTrucks:
    def __init__(self, app_data: ApplicationData):
        self._app_data = app_data

    def execute(self):
        return self._app_data.show_available_trucks()