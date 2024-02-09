from core.application_data import ApplicationData
from datetime import datetime, timedelta

class UpdateCurrentDayCommand:
    frozen_current_day_str = datetime.now().strftime("%Y-%m-%d-%H:%M")
    frozen_datetime_obj = datetime.strptime(frozen_current_day_str, "%Y-%m-%d-%H:%M")
    frozen_time = frozen_datetime_obj
    def __init__(self, params, app_data: ApplicationData):
        self.params = params
        self.app_data = app_data
        self._updated_day = None

    def execute(self):
        add_days = float(self.params[0])
        if add_days < 0:
            raise ValueError("Cannot return to the past, you can only add days")

        UpdateCurrentDayCommand.frozen_time += timedelta(days=add_days)
        return f"Current day is now {str(self.frozen_time)}"
