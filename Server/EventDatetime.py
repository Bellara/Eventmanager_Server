__author__ = 'Henning'

import datetime as dt

class EventDatetime():

    DATETIME_STRFORMAT = "%Y-%d-%m %H:%M"

    def __init__(self, d=None):
        self.d = d

    def fromString(self, s):
        self.d = dt.datetime.strptime(s, EventDatetime.DATETIME_STRFORMAT)

    def getDatetime(self):
        return self.d

    def __str__(self):
        return self.d.strftime(EventDatetime.DATETIME_STRFORMAT)