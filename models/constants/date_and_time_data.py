from datetime import timedelta
from models.constants.distance_data import Distance


def calculate_travel_time(departure_city, arrival_city):
    speed = 87
    distance = Distance.find_distance(departure_city, arrival_city)
    time = distance / speed
    return timedelta(hours=time)

def format_date(date):
    suffix_list = ["th", "st", "nd", "rd"] + ["th"] * 6
    day = date.day
    if 11 <= day <= 13:
        suffix = "th"
    else:
        suffix = suffix_list[day % 10]
    formatted_date = date.strftime(f"%b {day}{suffix} %H:%Mh")
    return formatted_date