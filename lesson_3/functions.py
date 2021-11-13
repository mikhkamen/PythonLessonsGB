def is_number(string):
    if string.isdigit():
        return int(string)
    else:
        try:
            float(string)
            return float(string)
        except ValueError:
            return string
