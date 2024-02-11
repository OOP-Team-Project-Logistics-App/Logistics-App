from models.constants.date_and_time_data import update_current_day


class UpdateCurrentDayCommand:
    def __init__(self, params):
        self.add_days = float(params[0])

    def execute(self):
        current_day = update_current_day(self.add_days)
        return str(current_day)
