from utils_base.time_classes.Time import Time
from utils_base.time_classes.TimeFormat import TimeFormat


def get_date_id():
    return TimeFormat.DATE_ID.stringify(Time.now())
