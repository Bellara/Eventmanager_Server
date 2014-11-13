__author__ = 'Henning'

from Password import Password

class User:

    SPALTE_ID = "id"
    SPALTE_NAME = "name"
    SPALTE_VORNAME = "vorname"
    SPALTE_MAIL = "mail"
    SPALTE_PW = "pw"

    def __init__(self, id=None, mail=None, name=None, vorname=None, pw=None):
        self.id = id
        self.mail = mail
        self.name = name
        self.vorname = vorname
        if pw != None:
            self.pw = Password(pw)
        else:
            self.pw = None

    @staticmethod
    def getAll():
        #Alle User Objekte von der Datenbank holen
        return

    def login(self, pw):
        #passwortpruefung
        if self.pw.getHash == Password(pw).getHash():
            return True
        else:
            return False

    @staticmethod
    def getByMail(m):
        #user Objekt anhand der Mail zurueckgeben
        return

    def register(self):
        #Alle params uebergeben?

        #pruefen ob schon ein element mit mail = sdfsf exisitiert

        #benutzer anlegen
        return

    def getasdict(self, attr=[]):
        ret = {}

        if len(attr) == 0:
            attr = ["mail", "vorname", "name", "id"]

        if "mail" in attr:
            ret["mail"] = self.mail

        if "name" in attr:
            ret["name"] = self.name

        if "vorname" in attr:
            ret["vorname"] = self.vorname

        if "id" in attr:
            ret["id"] = self.id

        return ret

    @staticmethod
    def getById():
        #User Objekt anhand der ID bekommen
        return