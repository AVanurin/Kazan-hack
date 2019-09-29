import handlers
from datetime import datetime


def register(object, content):
    start_date = str(datetime.now())
    return handlers._register_new_appeal(object, content, start_date)
