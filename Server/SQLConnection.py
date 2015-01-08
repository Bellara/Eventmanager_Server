from globals import *
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
        except ConfigParser.Error() as e:
            if DEBUG:
                raise EventError(str(e))
            else:
                raise EventError(EventError.CONFIG_PROBLEMS)

        try:
            self.dbconn = mysql.connector.connect(user=self.dbuser,
                                                  password=self.dbpw,
                                                  database=self.dbname
                                                  )
        except Exception as e:
            if DEBUG:
                raise EventError(str(e))
            else:
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

        try:
            c.execute(q, args)
            self.dbconn.commit()
            c.close()

        except Exception as e:
            c.close()
            if DEBUG:
                raise EventError(str(e))
            else:
                raise EventError(EventError.DB_DATA_PROBLEMS)

        return

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
            if DEBUG:
                raise EventError(str(e))
            else:
                raise EventError(EventError.DB_DATA_PROBLEMS)

        return rid

    def delete(self, q, args):
        c = self._getcursor()
        if c is None:
            raise EventError(EventError.DB_PROBLEMS)

        try:
            c.execute(q, args)
            self.dbconn.commit()
            c.close()
        except Exception as e:
            c.close()
            if DEBUG:
                raise EventError(str(e))
            else:
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
            if DEBUG:
                raise EventError(str(e))
            else:
                raise EventError(EventError.DB_DATA_PROBLEMS)

        return ret

    def _getcursor(self):
        if self.dbconn != None:
            try:
                return self.dbconn.cursor()
            except Exception as e:
                return None

    def close(self):
        if self.dbconn.is_connected():
            self.dbconn.close()

    @staticmethod
    def getInstance():
        if SQLConnection.Instance == None:
            SQLConnection.Instance = SQLConnection()
        return SQLConnection.Instance