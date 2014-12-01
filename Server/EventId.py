__author__ = 'Henning'

from hashids import Hashids

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
        self.id = hasher.decrypt(h)[0]

    def getUnhashed(self):
        return self.id

    def getHashed(self):
        hasher = Hashids()
        return hasher.encrypt(self.id, EventId.GLOBAL_SALT)
