from datetime import datetime


def get_current_date_as_integer():
    current_date = datetime.now().timestamp()
    return int(current_date)