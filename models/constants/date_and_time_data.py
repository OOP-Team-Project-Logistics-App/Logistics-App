from datetime import timedelta
from models.constants.distance_data import Distance


def calculate_travel_time(departure_city, arrival_city):
    speed = 87
    distance = Distance.find_distance(departure_city, arrival_city)
    time = distance / speed
    return timedelta(hours=time)

def format_date(date):
    """
    This function formats a datetime object into a string representation with a specific format. \
    It formats the date with suffixes(for example st, nd, rd, th).

        Parameters:
                date (datetime): The datetime object to be formatted.

        Returns:
                str: The formatted date string.
    """
    suffix_list = ["th", "st", "nd", "rd"] + ["th"] * 6
    day = date.day
    if 11 <= day <= 13:
        suffix = "th"
    else:
        suffix = suffix_list[day % 10]
    formatted_date = date.strftime(f"%b {day}{suffix} %H:%Mh")
    return formatted_date