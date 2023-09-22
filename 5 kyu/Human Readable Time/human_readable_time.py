def make_readable(seconds):
    seconds_hour = 60 * 60

    hours = seconds // seconds_hour
    seconds -= seconds_hour * hours

    minutes = seconds // 60
    seconds -= 60 * minutes

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
