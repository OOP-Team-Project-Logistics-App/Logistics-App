from core.application_data import ApplicationData


def try_parse_int(s):
    try:
        return int(s)
    except:
        raise ValueError("Invalid value. It must be an integer.")

def try_parse_float(s):
    try:
        return float(s)
    except:
        raise ValueError("Invalid value. It must be a number.")

def validate_login(app_data: ApplicationData, requires_login: bool):
    if requires_login and not app_data.has_logged_in_user:
        raise ValueError("User isn't logged in.")