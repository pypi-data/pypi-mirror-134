def check_bool(string=str()):
    string = str(string)
    return True if string.capitalize() == "True" or string.lower() == "true" or "True" in string or "true" in string else False