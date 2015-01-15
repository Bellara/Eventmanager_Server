__author__ = 'Henning'

from User import User
from Event import Event
from EventError import EventError
from SQLConnection import SQLConnection
from EventId import EventId


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
        if not isinstance(self.id, EventId) or \
            not isinstance(self.event, Event) or \
            not isinstance(self.user, User):
            raise EventError("sdasd")

        #status auf Invitation.NO setzen
        db = SQLConnection.getInstance()
        db.update("UPDATE invitations SET status=%s WHERE id=%s",
            (Invitation.YES, self.id.getUnhashed()))

        return

    def notcoming(self):
        #alle parameter pruefen
        if not isinstance(self.id, EventId) or \
            not isinstance(self.event, Event) or \
            not isinstance(self.user, User):
            raise EventError("sdfsdf")

        #status auf Invitation.NO setzen
        db = SQLConnection.getInstance()
        db.update("UPDATE invitations SET status=%s WHERE id=%s",
            (Invitation.NO, self.id.getUnhashed()))

        return

    def create(self):
        #alle parameter pruefen
        self.id = None

        if not isinstance(self.event, Event) or \
            not isinstance(self.user, User) or \
            type(self.status) is not int:
            raise EventError(EventError.UNDEFINED)

        db = SQLConnection.getInstance()

        if Invitation.fromUserAndEvent(self.user, self.event) is not None:
            raise EventError("Einladung bereits vorhanden.")

        id = db.insert("INSERT INTO invitations (user, event, status) VALUES (%s, %s, %s)", \
                       (self.user.id.getUnhashed(),
                       self.event.id.getUnhashed(),
                       self.status))

        self.id = EventId()
        self.id.setUnhashed(id)

        return

    @staticmethod
    def getAllForEvent(event):
        ret = []

        #DB Verbindung
        db = SQLConnection.getInstance()

        #SQL Befehl
        db_ret = db.select("SELECT * FROM invitations WHERE event=%s", (event.id.getUnhashed(),))

        #for schleife durch array
        for e in db_ret:
            i = Invitation()
            i.id = EventId()
            i.id.setUnhashed(int(e[0]))
            u_id = EventId()
            u_id.setUnhashed(int(e[1]))
            i.user = User.getById(u_id)
            i.event = event
            i.status = int(e[3])
            ret.append(i)

        return ret

    @staticmethod
    def getAllFromUser(user):
        ret = []

        #DB Verbindung
        db = SQLConnection.getInstance()

        #SQL Befehl
        db_ret = db.select("SELECT * FROM invitations WHERE user=%s", (user.id.getUnhashed(),))


        #for schleife durch array
        for e in db_ret:
            i = Invitation()
            i.id = EventId()
            i.id.setUnhashed(int(e[0]))
            i.id = e[0]
            i.user = user
            e_id = EventId()
            e_id.setUnhashed(int(e[2]))
            i.event = Event.getById(e_id)
            i.status = int(e[3])
            ret.append(i)

        return ret

    def getAsDict(self, attr=[]):
        ret = {}

        if len(attr) == 0:
            attr=["event", "status", "user", "id"]

        if "id" in attr:
            ret["id"] = str(self.id.getHashed())
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
                           (user.id.getUnhashed(), event.id.getUnhashed()))

        if len(db_ret) > 1:
            raise EventError(EventError.UNDEFINED)

        if len(db_ret) == 0:
            return None

        db_ret = db_ret[0]

        ret.id = EventId()
        ret.id.setUnhashed(db_ret[0])
        uid = EventId()
        uid.setUnhashed(db_ret[1])
        ret.user = User.getById(uid)
        eid = EventId()
        eid.setUnhashed(db_ret[2])
        ret.event = Event.getById(eid)
        ret.status = int(db_ret[3])

        return ret

