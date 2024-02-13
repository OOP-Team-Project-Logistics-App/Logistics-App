from datetime import timedelta
from commands.validators.validation_helpers import try_parse_float
from core.application_data import ApplicationData


class UpdateCurrentDayCommand:
    def __init__(self, params: list, app_data: ApplicationData):
        self.add_days = try_parse_float(params[0])
        self.app_data = app_data

    def execute(self):
        return self.app_data.update_current_day(self.add_days)