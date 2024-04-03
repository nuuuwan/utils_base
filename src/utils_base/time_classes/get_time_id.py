from utils_base.time_classes.Time import Time
from utils_base.time_classes.TimeFormat import TimeFormat


def get_time_id():
    return TimeFormat.TIME_ID.stringify(Time.now())
