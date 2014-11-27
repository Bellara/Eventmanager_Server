__author__ = 'Henning'

from User import User
from Event import Event
from EventError import EventError
from SQLConnection import SQLConnection

class Invitation:

    SPALTE_ID = "id"
    SPALTE_USER = "user"
    SPALTE_EVENT = "event"
    SPALTE_STATUS = "status"

    UNDECIDED = 0
    YES = 1
    NO = 2

    def __init__(self, id=None, user=None, event=None, status=UNDECIDED):
        self.id = id
        self.user = user
        self.event = event
        self.status = status


    def signin(self):
        if type(self.id) is not int or \
            not isinstance(self.event, Event) or \
            not isinstance(self.user, User):
            raise EventError(EventError.UNDEFINED)

        #status auf Invitation.NO setzen
        db = SQLConnection.getInstance()
        db.update("UPDATE invitations SET status=%s WHERE id=%s",
            (Invitation.YES, self.id))

        return

    def notcoming(self):
        #alle parameter pruefen
        if type(self.id) is not int or \
            not isinstance(self.event, Event) or \
            not isinstance(self.user, User):
            raise EventError(EventError.UNDEFINED)

        #status auf Invitation.NO setzen
        db = SQLConnection.getInstance()
        db.update("UPDATE invitations SET status=%s WHERE id=%s",
            (Invitation.NO, self.id))

        return

    def create(self):
        #alle parameter pruefen
        self.id = None

        if not isinstance(self.event, Event) or \
            not isinstance(self.user, User) or \
            type(self.status) is not int:
            raise EventError(EventError.UNDEFINED)

        db = SQLConnection.getInstance()

        id = db.insert("INSERT INTO invitations (user, event, status) VALUES (%s, %s, %s)", \
                       (self.user.id,
                       self.event.id,
                       self.status))

        self.id = id

        return

    @staticmethod
    def getAllForEvent(event):
        ret = []

        #DB Verbindung
        db = SQLConnection.getInstance()

        #SQL Befehl
        db_ret = db.select("SELECT * FROM invitations WHERE event=%s", (event.id,))

        #for schleife durch array
        for e in db_ret:
            i = Invitation()
            i.id = e[0]
            i.user = User.getById(e[1])
            i.event = Event.getById(e[2])
            i.status = int(e[3])
            ret.append(i)

        return ret

    @staticmethod
    def getAllFromUser(user):
        ret = []

        #DB Verbindung
        db = SQLConnection.getInstance()

        #SQL Befehl
        db_ret = db.select("SELECT * FROM invitations WHERE user=%s", (user.id,))

        #for schleife durch array
        for e in db_ret:
            i = Invitation()
            i.id = e[0]
            i.user = User.getById(e[1])
            i.event = Event.getById(e[2])
            i.status = int(e[3])
            ret.append(i)

        return ret

    def getAsDict(self, attr=[]):
        ret = {}

        if len(attr) == 0:
            attr=["event", "status", "user", "id"]

        if "id" in attr:
            ret["id"] = str(self.id)
        if "status" in attr:
            ret["status"] = str(self.status)
        if "user" in attr:
            ret["user"] = self.user.getAsDict()
        if "event" in attr:
            ret["event"] = self.event.getAsDict()

        return ret

    @staticmethod
    def getFromUserAndEvent(user, event):

        ret = Invitation()

        db = SQLConnection.getInstance()

        db_ret = db.select("SELECT * FROM invitations WHERE user=%s AND event=%s",
                           (user.id, event.id))

        if len(db_ret) is not 1:
            raise EventError(EventError.UNDEFINED)

        db_ret = db_ret[0]

        ret.id = db_ret[0]
        ret.user = User.getById(db_ret[1])
        ret.event = Event.getById(db_ret[2])
        ret.status = int(db_ret[3])

        return ret

