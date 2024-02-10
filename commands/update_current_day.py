from datetime import datetime, timedelta

class UpdateCurrentDayCommand:
    frozen_current_day_str = datetime.now().strftime("%Y-%m-%d-%H:%M")
    frozen_datetime_obj = datetime.strptime(frozen_current_day_str, "%Y-%m-%d-%H:%M")
    current_day = frozen_datetime_obj
    def __init__(self, params):
        self.params = params

    def execute(self):
        add_days = float(self.params[0])
        if add_days < 0:
            raise ValueError("Cannot return to the past, you can only add days")

        UpdateCurrentDayCommand.current_day += timedelta(days=add_days)
        return f"Current day is now {str(self.current_day)}"
