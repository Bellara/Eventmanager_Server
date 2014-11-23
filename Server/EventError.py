__author__ = 'Henning'

class EventError(Exception):
    DB_PROBLEMS = "Probleme bei Herstellen der Datenbankverbindung!"
    DB_DATA_PROBLEMS = "Probleme bei Holen der Daten aus der Datenbank!"
    NO_ADMIN = "Dieser User ist kein Admin des Events!"
    NO_USER_FOUND = "Der User wurde nicht gefunden"
    INVALID_MAIL = "Ungueltige Mail Adresse angegeben"
    INVALID_PASSWORD = "Passwort muss mindestens fuenf Zeichen lange sein"
    USER_ALREADY_EXISTING = "Ein Benutzer mit der Mail Adresse exisiter bereits"
    WRONG_PASSWORD = "Falsches Passwort"
    pass
