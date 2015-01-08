__author__ = 'Henning'

from Password import Password
from SQLConnection import SQLConnection
from EventError import EventError
from EventId import EventId
from EventMail import EventMail

class User:

    def __init__(self, id=None, mail=None, name=None, vorname=None, pw=None):
        self.id = id
        self.mail = EventMail(mail)
        self.name = name
        self.vorname = vorname
        if pw != None:
            self.pw = Password(pw)
        else:
            self.pw = None

    @staticmethod
    def getAll():
        #Alle User Objekte von der Datenbank holen
        db = SQLConnection.getInstance()
        db_content = db.select("SELECT * FROM user", ())

        ret = []

        for e in db_content:
            user = User()
            user.id = EventId()
            user.id.setUnhashed(int(e[0]))
            user.setMail(str(e[1]))
            pw = Password(h=str(e[2]))
            user.pw = pw
            user.setName(str(e[3]))
            user.setVorname(str(e[4]))

            ret.append(user)

        return ret

    def login(self, pw):
        return self.pw.getHash() == Password(pw).getHash()


    @staticmethod
    def getByMail(m):
        db = SQLConnection.getInstance()
        db_content = db.select("SELECT * FROM user WHERE mail=%s", (m,))

        if len(db_content) is 0:
            raise EventError(EventError.NO_USER_FOUND)

        elif len(db_content) > 1:
            raise Exception()

        else:
            db_content = db_content[0]
            user = User()
            user.id = EventId()
            user.id.setUnhashed(int(db_content[0]))
            user.setMail(str(db_content[1]))
            pw = Password(h=str(db_content[2]))
            user.pw = pw
            user.setName(str(db_content[3]))
            user.setVorname(str(db_content[4]))

            return user

    def register(self):
        #Alle params uebergeben?
        if (self.mail is not None) and \
            (self.pw is not None) and \
            (self.name is not None) and \
            (self.vorname is not None):
        #pruefen ob schon ein element mit mail = sdfsf exisitiert
            db = SQLConnection.getInstance()
            if db.count("SELECT COUNT(*) FROM user WHERE mail=%s", (self.mail,)) > 0:
                raise EventError(EventError.USER_ALREADY_EXISTING)

        #benutzer anlegen
            id = db.insert("INSERT INTO user (mail, pw, name, vorname) VALUES (%s,%s,%s,%s)", (self.mail,
                                                                                          self.pw.getHash(),
                                                                                          self.name,
                                                                                          self.vorname))
            self.id = EventId()
            self.id.setUnhashed(id)
        return

    def getAsDict(self, attr=[]):
        ret = {}

        if len(attr) == 0:
            attr = ["mail", "vorname", "name", "id"]

        if "mail" in attr:
            ret["mail"] = str(self.mail)

        if "name" in attr:
            ret["name"] = self.name

        if "vorname" in attr:
            ret["vorname"] = self.vorname

        if "id" in attr:
            ret["id"] = str(self.id.getHashed())

        return ret

    @staticmethod
    def getById(uid):
        #User Objekt anhand der ID bekommen
        db = SQLConnection.getInstance()
        db_content = db.select("SELECT * FROM user WHERE id=%s", (uid.getUnhashed(),))

        if len(db_content) is 0:
            raise EventError(EventError.NO_USER_FOUND)

        elif len(db_content) > 1:
            raise Exception()

        else:
            db_content = db_content[0]
            user = User()
            user.id = EventId()
            user.id.setUnhashed(int(db_content[0]))

            user.setMail(str(db_content[1]))
            pw = Password(h=str(db_content[2]))
            user.pw = pw
            user.setName(str(db_content[3]))
            user.setVorname(str(db_content[4]))
            return user

    def setMail(self, mail):
        """
        Einfache Ueberpruefung ob Mail eine 'vernuenftige' Mail Adresse ist.

        :param mail: Mail Adresse
        :return: <void>
        """
        email = EventMail(mail)

        if email.check() is False:
            raise EventError.INVALID_MAIL

        self.mail = email

        return

    def setPassword(self, pw):
        if len(pw) < 5:
            raise EventError(EventError.INVALID_PASSWORD)
        pw = Password(s=pw)
        self.pw = pw

        return

    def setName(self, n):
        #TODO ggf. Pruefungen machen
        self.name = n

        return

    def setVorname(self, v):
        #TODO ggf Pruefungen machen
        self.vorname = v
        return