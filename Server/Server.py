__author__ = 'Henning'

from User import User
from Event import Event
from Invitation import Invitation
from EventError import EventError
from EventDatetime import EventDatetime

class Server():
    """
    Hautpserverklasse zur Verarbeitung der Anfragen.
    In dieser Datei findet kein HTTP Parsing mehr statt.
    """

    def userLogin(self, mail, pw):
        """
        Methode zur Verarbeitung eines User Logins

        :param mail: Mail Adresse des einzuloggenden Users
        :param pw: Passwort des einzuloggenden users
        :return: Das entsprechende User Objekt als Dictionary
        """
        user = User.getByMail(mail)

        if user.login(pw):
            return user.getAsDict()
        else:
            raise EventError(EventError.WRONG_PASSWORD)

    def getAllUsers(self):
        """
        Methode zur Rueckgabe aller User Objekte

        :return: Array aus Dictionaries der User Objekte
        """
        ret = []

        users = User.getAll()

        for e in users:
            ret.append(e.getAsDict())

        return ret

    def getInvitations(self, userid):
        """
        Methoe zur Rueckgabe aller Einladungen eines Benutzers,
        auf die noch nicht geantwort wurde.

        :param userid: ID des Benutzers
        :return: Array aus Dicts aller Einladungen
        """

        ret = []

        user = User.getById(userid)
        invitations = Invitation.getAllFromUser(user)

        for e in invitations:
            ret.append(e.getAsDict())

        return ret

    def getEventById(self, eventid):
        """
        Methode zur Rueckgabe aller Informationen eines
        bestimmten Events.

        :param eventid: ID des Events
        :return: Alle Informationen eines Events in Form eines
        Dictionaries
        """

        event = Event.getById(eventid)
        return event.getAsDict()

    def createEvent(self, aid, time, bz, location):
        """
        Methode zur Anlegung eines neuen Events

        :param aid: ID des Users der als Admin eingetragen werden soll
        :param time: Datum und Zeit des Events als Datetime-Objekt
        :param bz: Bezeichnung fuer die Veranstaltung
        :param location: Ort der Veranstaltung
        :return: Event Objekt als Dictionary
        """

        event = Event()

        admin = User.getById(aid)
        event.admin = admin

        date = EventDatetime()
        date.fromString(time)
        event.datetime = date

        event.description = bz

        event.location = location

        event.create()

        return event.getAsDict()


    def deleteEvent(self, aid, eventid):
        """
        Methode zur Loeschung eines Events

        :param eventid: ID des Events, welches geloescht werden soll.
        :param aid: ID des Admins des Events um nur dem Admin zu erlauben sein Event zu loeschen.
        :return: -
        """

        event = Event.getById(eventid)
        user = User(id=aid)
        if not event.authorized(user):
            raise EventError(EventError.USER_NOT_AUTHORIZED)

        event.delete()

        return

    def invite(self, eventid, aid, uid):
        """
        Methode zum Einladen eines Benutzers.

        :param eventid: ID des Events, fuer das eingeladen werden soll.
        :param aid: ID des Admin des Events zu Sicherheitszwecken.
        :param uid: Einzuladener User
        :return: -
        """

        event = Event.getById(eventid)
        if not event.isAdmin(aid):
            raise EventError(EventError.NO_ADMIN)

        user = User.getById()

        invitation = Invitation(user=user, event=event)
        invitation.create() #TODO Methode zum Speichern der Einladung

        return

    def registerUser(self, mail, name, vorname, pw):
        """
        Methode zur Registration eines neuen Users.

        :param mail: Mail des neuen Users
        :param name: Name des neuen Users
        :param vorname: Vorname des neuen Users
        :param pw: Passwort des neuen Users
        :return: User Objekt als Dictionary
        """
        newuser = User()
        newuser.setMail(mail) #TODO Methoden anlegen, damit Pruefungen stattfinden koennen.
        newuser.setName(name)
        newuser.setVorname(vorname)
        newuser.setPassword(pw)

        newuser.register()

        return newuser.getAsDict()

    def signin(self, eventid, userid, status):
        """
        Methode zur Anmeldung/Absage eines Events

        :param eventid: ID des Events
        :param userid: ID des Users
        :param status: neuer Status
        :return:  -
        """
        user = User.getById(userid)
        event = Event.getById(eventid)

        invitation = Invitation.getFromUserAndEvent(user, event)

        if status == Invitation.YES:
            invitation.signin()
        elif status == Invitation.NO:
            invitation.notcoming()
        else:
            #Niemand wird ein Anfrage senden um zu sagen, dass er sich noch nicht entschschieden hat.
            pass

        return





