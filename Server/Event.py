__author__ = 'Henning'

class Event:

    SPALTE_ID = "id"
    SPALTE_LOCATION = "location"
    SPALTE_DESCRIPTION = "description"
    SPALTE_DATETIME = "datetime"
    SPALTE_ADMIN = "admin"

    def __init__(self, id=None, location=None, description=None, datetime=None, admin=None):
        self.id = id
        self.location = location
        self.description = description
        self.datetime = datetime
        self.admin = admin

        return