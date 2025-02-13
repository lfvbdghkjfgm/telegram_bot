from datetime import datetime
import time


def time_now():
    time_1 = datetime.fromtimestamp(time.time())
    month = time_1.month
    day = time_1.day
    week = time_1.strftime('%A').lower()
    com_time = (time_1.hour+3) * 60 + time_1.minute
    return [month, day, week, com_time]
