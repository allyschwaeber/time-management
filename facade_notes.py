import logging
import ddl
import dml
import kronos
import facade_abc
import os


class NotesFacade(facade_abc.AbcFacade):
    __rows_in_table = 0

    def __init__(self, database):
        self.db = database
        self.ddl = ddl.DataDefinitionLanguage(database)
        self.dml = dml.DataManipulationLanguage(database)
        self.table_name = "notes"
        NotesFacade.__rows_in_table = self.count_rows()
        try:
            self.schema = ddl.DataDefinitionLanguage.parse_json(
                os.path.join(
                    os.path.dirname(__file__),
                    "table_schemas/" + self.table_name + ".json",
                )
            )
        except ValueError:
            logging.error("Unable to parse schema")

    def count_rows(self):
        return len(self.get_rows())

    def get_rows(self):
        return self.dml.select_star_sql(self.table_name)

    def delete_history(self):
        self.ddl.drop_table(self.table_name)

    def disconnect(self):
        self.db.disconnect()

    def get_last_workday(self):
        rows = []
        for row in self.get_rows():
            if kronos.get_day_of_week(kronos.get_date_time()) == "Monday":
                if kronos.is_previous_friday(row[3]):
                    rows.append(row)
            if kronos.is_yesterday(row[3]):
                rows.append(row)
        return rows

    def insert_note(self, note):
        NotesFacade.increment_row_count()
        self.db.get_connection().execute(
            "INSERT INTO {} ({}, {}, {}, {}) VALUES (?, ?, ?, ?)".format(
                self.table_name, *self.schema
            ),
            (
                NotesFacade.__rows_in_table,
                "NOTE",
                note,
                kronos.get_date_time_as_string(),
            ),
        )
        self.db.get_connection().commit()

    @classmethod
    def reset_row_count(cls):
        NotesFacade.__rows_in_table = 0

    @classmethod
    def increment_row_count(cls):
        NotesFacade.__rows_in_table = NotesFacade.__rows_in_table + 1
