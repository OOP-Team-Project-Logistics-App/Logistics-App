from datetime import datetime
from models.constants.distances import Distance

class CreateDeliveryRouteCommand:
    id = 1
    pass  # id += 1

    def __init__(self, params, app_data):
        self.params = params
        self.app_data = app_data

    def execute(self):
        route_times = {} #key = city, value = datetime
        for i in range(0,len(self.params), 2):
            city = self.params[i]
            time = self.params[i+1]
            result_datetime = datetime.strptime(f"2024-{time}", "%Y-%m:%d:%H")
            route_times[city] = result_datetime
        start_city = (next(iter(route_times)))
        for key,value in route_times.items():
            distance_between_cities = Distance.find_distance(start_city, key)
            start_city = key
            print(distance_between_cities)
        #maximum average speed = 87km/h
        #maximum travel time per day = 11h



        # check if we have expected number of parameters, if yes, assign parameters
        return print(route_times)

