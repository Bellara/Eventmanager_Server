__author__ = 'Henning'

class EventError(Exception):
    DB_PROBLEMS = "Probleme bei Herstellen der Datenbankverbindung!"
    DB_DATA_PROBLEMS = "Probleme bei Holen der Daten aus der Datenbank!"
    NO_ADMIN = "Dieser User ist kein Admin des Events!"
    pass
