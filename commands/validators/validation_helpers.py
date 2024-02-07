def try_parse_int(s):
    try:
        return int(s)
    except:
        raise ValueError("Invalid value for weight. It must be an integer.")