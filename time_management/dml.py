import logging


class DataManipulationLanguage:
    def __init__(self, database):
        self.__database = database
        self.__connection = database.get_connection()
        self.__cursor = database.get_cursor()

    def select_star_sql(self, table):
        query = f"SELECT * FROM {table}"
        try:
            self.__cursor.execute(query)
        except ValueError:
            logging.error("Unable to execute query!")
        return self.__cursor.fetchall()

    def arbitrary_select(self, fields, table, conditions):
        query = f"SELECT {fields} FROM {table} WHERE {conditions}"
        try:
            self.__cursor.execute(query)
        except ValueError:
            logging.error("Unable to execute query!")
        return self.__cursor.fetchall()
