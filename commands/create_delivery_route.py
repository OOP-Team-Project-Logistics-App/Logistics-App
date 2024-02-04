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
            start_city_time = route_times[start_city]
            distance_between_cities = Distance.find_distance(start_city, key)
            travel_time_between_cities = value - start_city_time
            days = travel_time_between_cities.days
            seconds = travel_time_between_cities.seconds
            travel_time_in_hours_only = (days * 24) + (seconds // 3600)
            if travel_time_in_hours_only > 0:
                average_speed = distance_between_cities/travel_time_in_hours_only
                if average_speed > 87:
                    raise ValueError(f"Travel time between {start_city} and {key} must be longer")
                print(average_speed)
            start_city = key
        #maximum average speed = 87km/h


        # check if we have expected number of parameters, if yes, assign parameters
        return print(route_times)

