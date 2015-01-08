__author__ = 'Henning'

from EventError import EventError
import re

class EventMail():

    MAIL_REGEX_STRING = "^.+@[^\.].*\.[a-z]{2,}$"

    def __init__(self, s):
        self.s = s

    def check(self):
        r = re.compile(EventMail.MAIL_REGEX_STRING)
        if r.search(self.s) is None:
            return False
        return True

    def getHost(self):
        parts = self.s.split("@")

        if len(parts) != 2:
            raise EventError(EventError.INVALID_MAIL)

        else:
            return parts[1]

    def getMailUser(self):
        parts = self.s.split("@")

        if len(parts) != 2:
            raise EventError(EventError.INVALID_MAIL)

        else:
            return parts[0]

    def __str__(self):
        return self.s
