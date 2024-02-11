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