import json
import os


class DataDefinitionLanguage:
    __schemas_path = os.path.join(os.path.dirname(__file__), "table_schemas/")

    def __init__(self, database):
        self.__database = database
        self.__connection = database.get_connection()
        self.__cursor = database.get_cursor()

    def __strip_brackets_and_colons(self, query):
        return query.replace("{", "").replace("}", "").replace(":", "")

    def __create_sql(self, table, schema):
        query = f"CREATE TABLE IF NOT EXISTS {table} ({schema})"
        return self.__strip_brackets_and_colons(query)

    def create_table(self, table, schema):
        self.__cursor.execute(self.__create_sql(table, schema))
        self.__connection.commit()

    def drop_table(self, table):
        query = f"DROP TABLE {table}"
        self.__cursor.execute(query)

    def create_all_tables(self):
        schema_files = DataDefinitionLanguage.list_schemas()
        for schema in schema_files:
            schema_contents = DataDefinitionLanguage.parse_json(
                DataDefinitionLanguage.__schemas_path + schema
            )
            table_name = schema.replace(".json", "")
            self.create_table(table_name, schema_contents)

    @staticmethod
    def parse_json(path):
        with open(path) as file:
            data = json.load(file)
        return data

    @staticmethod
    def list_schemas():
        return [
            pos_json
            for pos_json in os.listdir(DataDefinitionLanguage.__schemas_path)
            if pos_json.endswith(".json")
        ]
