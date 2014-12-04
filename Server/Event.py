__author__ = 'Henning'

from SQLConnection import SQLConnection
from EventError import EventError
from EventDatetime import EventDatetime
from User import User
from EventId import EventId

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

    @staticmethod
    def getById(id):
        event = Event()
        db = SQLConnection.getInstance()

        db_content = db.select("SELECT * FROM events WHERE id=%s", (id.getUnhashed(),))

        if len(db_content) < 1:
            raise EventError(EventError.NO_EVENT_FOUND)

        db_event = db_content[0]

        event.id = EventId()
        event.id.setUnhashed(int(db_event[0]))
        event.location = db_event[1]
        event.datetime = EventDatetime(db_event[2])

        admin_id = EventId()
        admin_id.setUnhashed(int(db_event[3]))
        admin = User.getById(admin_id)

        event.admin = admin
        event.description = db_event[4]

        return event

    def create(self):
        #aktuelle Parameter pruefen
        self.id = None

        if not isinstance(self.admin, User) or \
            type(self.description) is not str or \
            not isinstance(self.datetime, EventDatetime) or \
            type(self.location) is not str:
            raise Exception(EventError.UNDEFINED) #Unbekannter internet Fehler

        #in die Datenbank einpflegen.
        db = SQLConnection.getInstance()

        id = db.insert("INSERT INTO events (location, time, admin, description) VALUES (%s,%s,%s,%s)",
            (self.location, str(self.datetime), self.admin.id.getUnhashed(), self.description))

        self.id = EventId()
        self.id.setUnhashed(int(id))

        return

    def delete(self):
        #ist id gefuellt?
        if self.id is None:
            raise EventError(EventError.UNDEFINED)


        db = SQLConnection.getInstance()
        db.delete("DELETE FROM events WHERE id=%s", (self.id.getUnhashed(),))

        #TODO Zusaetzlich noch alle Einladungen fuer dieses Element anfragen und loeschen...
        return

    def getAsDict(self, attr=[]):
        ret = {}

        if len(attr) == 0:
            attr = ["eid", "ort", "bezeichnung", "zeit", "admin"]

        if "eid" in attr:
            ret["eid"] = str(self.id.getHashed())

        if "ort" in attr:
            ret["ort"] = self.location

        if "bezeichnung" in attr:
            ret["bezeichnung"] = self.description

        if "zeit" in attr:
            ret["zeit"] = str(self.datetime)

        if "admin" in attr:
            ret["admin"] = self.admin.getAsDict()

        return ret


    def authorized(self, user):
        """
        Methode zur Ueberpruefeng, ob ein User Admin des Events ist.

        :param aid: ID des abzufragenden Users.
        :return: True: User(aid) ist Admin. False: User(aid) ist kein Admin
        """

        return self.admin.id.getUnhashed() == user.id.getUnhashed()
