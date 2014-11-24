from globals import CONFIG_PATH
import ConfigParser
import mysql.connector
from EventError import EventError


class SQLConnection():

    CONFIG_SECTION = "Database"
    Instance = None

    def __init__(self):
        try:
            config = ConfigParser.ConfigParser()
            config.read(CONFIG_PATH)
            self.dbuser = config.get(SQLConnection.CONFIG_SECTION, "user")
            self.dbpw = config.get(SQLConnection.CONFIG_SECTION, "pw")
            self.dbip = config.get(SQLConnection.CONFIG_SECTION, "ip")
            self.dbport = config.get(SQLConnection.CONFIG_SECTION, "port")
            self.dbname = config.get(SQLConnection.CONFIG_SECTION, "db")
        except ConfigParser.Error():
            raise Exception("Probleme beim Laden der Datenbankeinstellungen!")

        try:
            self.dbconn = mysql.connector.connect(user=self.dbuser,
                                                  password=self.dbpw,
                                                  database=self.dbname
                                                  )
            mysql.connector.connect()
        except Exception:
            raise EventError("Probleme beim Hersellen der Datenbankverbindung")

        return

    def select(self, q, args):
        c = self._getcursor()
        if c is None:
            raise EventError(EventError.DB_PROBLEMS)

        try:
            data = []
            c.execute(q, args)
            for e in c:
                data.append(e)
            c.close()
        except Exception as e:
            c.close()
            raise EventError(str(e))

        return data

    def update(self, q, args):
        c = self._getcursor()
        if c is None:
            raise EventError(EventError.DB_PROBLEMS)
        pass

    def insert(self, q, args):
        c = self._getcursor()
        if c is None:
            raise EventError(EventError.DB_PROBLEMS)

        try:
            c.execute(q, args)
            rid = c.lastrowid
            self.dbconn.commit()
            c.close()

        except Exception as e:
            c.close()
            raise EventError(str(e))

        return rid

    def delete(self, q, args):
        c = self._getcursor()
        if c is None:
            raise EventError(EventError.DB_PROBLEMS)

        try:
            c.execute(q, args)
            self.dbconn.commit()
            c.close()
        except Exception:
            c.close()
            raise EventError(EventError.DB_DATA_PROBLEMS)

    def count(self, q, args):
        c = self._getcursor()
        if c is None:
            raise EventError(EventError.DB_PROBLEMS)

        try:
            c.execute(q, args)
            for e in c:
                ret = int(e[0])

            c.close()
        except Exception as e:
            c.close()
            raise EventError(str(e))

        return ret

    def _getcursor(self):
        if self.dbconn != None:
            try:
                return self.dbconn.cursor()
            except:
                return None

    @staticmethod
    def getInstance():
        if SQLConnection.Instance == None:
            SQLConnection.Instance = SQLConnection()
        return SQLConnection.Instance