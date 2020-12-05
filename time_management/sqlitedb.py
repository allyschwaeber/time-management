import sqlite3
import logging


class SQLiteDatabase:
    """SQLiteDatabase is a wrapper for a SQLite Database's name, connection, and cursor.
    TODO :: Determine the correct Singleton pattern to apply to this class, IFF the pattern should be applied.
    """

    def __init__(self, db_name=":memory:"):
        try:
            self.__db_name = db_name
            self.__connection = sqlite3.connect(self.__db_name)
            self.__cursor = self.__connection.cursor()
        except ValueError:
            logging.error("Unable to initialize database!")

    def get_db_name(self):
        return self.__db_name

    def get_connection(self):
        return self.__connection

    def get_cursor(self):
        return self.__cursor

    def list_tables(self):
        self.get_cursor().execute('SELECT name from sqlite_master where type= "table"')
        return self.get_cursor().fetchall()

    def disconnect(self):
        self.get_connection().close
