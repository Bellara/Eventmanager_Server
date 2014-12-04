__author__ = 'Henning'

from utils.hashids import Hashids
from EventError import EventError

class EventId:
    """
    Hilfsklasse zur 'verschluesselung' von IDs
    """

    GLOBAL_SALT = 13377331

    def __init__(self):
        self.id = None

    def setUnhashed(self, u):
        self.id = u

    def setHashed(self, h):
        hasher = Hashids()
        try:
            self.id = hasher.decrypt(h)[0]
        except:
            raise EventError(EventError.INVALID_ID)

    def getUnhashed(self):
        return self.id

    def getHashed(self):
        hasher = Hashids()
        return hasher.encrypt(self.id, EventId.GLOBAL_SALT)
