__author__ = 'Henning'

import hashlib

class Password:
    def __init__(self, s = None, h = None):
        self.string = s
        if self.string != None:
            temph = hashlib.sha256()
            temph.update(self.string)
            self.h = temph.hexdigest()
        else:
            self.h = h

    def getHash(self):
        return self.h

    def getString(self):
        return self.string