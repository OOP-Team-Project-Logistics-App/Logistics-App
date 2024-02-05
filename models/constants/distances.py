class Distance:
    distances_matrix = [
        [0, 877, 1376, 2762, 909, 3935, 4016],
        [877, 0, 725, 2255, 1765, 3752, 3509],
        [1376, 725, 0, 1530, 1927, 3027, 2785],
        [2762, 2255, 1530, 0, 2993, 1497, 2481],
        [909, 1765, 1927, 2993, 0, 3426, 4311],
        [3935, 3752, 3027, 1497, 3426, 0, 4025],
        [4016, 3509, 2785, 2481, 4311, 4025, 0]
    ]

    @classmethod
    def find_distance(cls, departure_city, arrival_city):
        cities = ["Sydney", "Melbourne", "Adelaide", "Alice_Springs", "Brisbane", "Darwin", "Perth"]
        departure_city_idx = cities.index(departure_city)
        arrival_city_idx = cities.index(arrival_city)
        return cls.distances_matrix[departure_city_idx][arrival_city_idx]