__author__ = 'Henning'

class Invitation:

    SPALTE_ID = "id"
    SPALTE_USER = "user"
    SPALTE_EVENT = "event"
    SPALTE_STATUS = "status"

    UNDECIDED = 0
    YES = 1
    NO = 2

    def __init__(self, id=None, user=None, event=None, status=None):
        self.id = id
        self.user = user
        self.event = event
        self.status = status


    def signin(self):
        #alle parameter pruefen

        #status auf Invitation.YES setzen

        #SQL Update
        pass

    def notcoming(self):
        #alle parameter pruefen

        #status auf Invitation.NO setzen

        #SQL Update
        pass

    def create(self):
        #alle parameter pruefen

        #SQL INSERT
        pass

    @staticmethod
    def getAllFromUser(user):
        #SQL abfrage
        pass