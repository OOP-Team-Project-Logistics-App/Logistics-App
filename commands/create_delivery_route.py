from datetime import datetime


class CreateDeliveryRouteCommand:
    id = 1
    pass  # id += 1

    def __init__(self, params, app_data):
        self.params = params
        self.app_data = app_data

    def execute(self):
        route_times = {}
        for i in range(0,len(self.params), 2):
            city = self.params[i]
            time = self.params[i+1]
            result_datetime = datetime.strptime(f"2024-{time}", "%Y-%m:%d:%H")
            route_times[city] = result_datetime
        # check if we have expected number of parameters, if yes, assign parameters
        return print(route_times)

