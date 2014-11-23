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

    @staticmethod
    def getById():
        #Daten von der Datenbank holen.
        pass

    def invite(self, user):
        #Ist User schon eingeladen?

        #Invitation anlegen

        #Invitation speichern
        pass

    def create(self):
        #aktuelle Parameter pruefen

        #in die Datenbank einpflegen.
        pass

    def delete(self):
        #ist id gefuellt?

        #loeschen !!Einladungen auch loeschen!!
        pass

    def getAsDict(self, attr=[]):
        ret = {}

        if len(attr) == 0:
            attr = ["eid", "ort", "bezeichnung", "zeit", "admin"]

        if "eid" in attr:
            ret["eid"] = self.id

        if "ort" in attr:
            ret["ort"] = self.location

        if "bezeichnung" in attr:
            ret["bezeichnung"] = self.description

        if "zeit" in attr:
            ret["zeit"] = str(self.datetime)

        if "admin" in attr:
            ret["admin"] = self.admin.getAsDict()

        return ret

    def getInvitationFromUser(self, u):
        #Einladung pullen bei der eid = self.id und uid = self.uid
        pass

    def authorized(self, aid):
        """
        Methode zur Ueberpruefeng, ob ein User Admin des Events ist.

        :param aid: ID des abzufragenden Users.
        :return: True: User(aid) ist Admin. False: User(aid) ist kein Admin
        """
