class CreateDeliveryRouteCommand:
    id = 1
    pass #id += 1

    def start_location(self):
        pass

    def departure_time(self):
        #first_location of delivery_route has departure_time, departure time cannot be in the past
        pass


    def expected_arrival_time(self):
        #all locations after start_location have expected_arrival_time, arrival time cannot force the average speed between locations to exceed 87km/h
        pass


    def delivery_route(self):
        #at least 2 locations(start and end location)
        pass

    def total_distance_of_route(self):
        #total distance must be shorter than 13000km
        pass

    def __str__(self):
        #- {start_location} → {other_locations, any number as long as total distance shorter than 13000km} → {end_location}
        pass