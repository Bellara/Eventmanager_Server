__author__ = 'Henning'

import datetime as dt
from EventError import EventError

class EventDatetime():

    DATETIME_STRFORMAT = "%Y-%m-%d %H:%M"

    def __init__(self, d=None):
        self.d = d

    def fromString(self, s):
        try:
            self.d = dt.datetime.strptime(s, EventDatetime.DATETIME_STRFORMAT)
        except:
            raise EventError(EventError.WRONG_DATE_FORMAT)

    def getDatetime(self):
        return self.d

    def __str__(self):
        return self.d.strftime(EventDatetime.DATETIME_STRFORMAT)