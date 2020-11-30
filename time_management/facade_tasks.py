import logging
import ddl
import dml
import kronos
import facade_abc
import os


class TasksFacade(facade_abc.AbcFacade):
    __rows_in_table = 0

    def __init__(self, database):
        self.db = database
        self.ddl = ddl.DataDefinitionLanguage(database)
        self.dml = dml.DataManipulationLanguage(database)
        self.table_name = "tasks"
        TasksFacade.__rows_in_table = self.count_rows()
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

    def get_ids(self):
        ids = []
        for row in self.get_rows():
            ids.append(row[0])
        return ids

    def get_last_workday(self):
        rows = []
        for row in self.get_rows():
            if kronos.get_day_of_week(kronos.get_date_time()) == "Monday":
                if kronos.is_previous_friday(row[3]):
                    rows.append(row)
            if kronos.is_yesterday(row[3]):
                rows.append(row)
        return rows

    def complete_task(self, row_id):
        now = kronos.get_date_time_as_string()
        self.db.get_cursor().execute(
            f"UPDATE {self.table_name} SET is_complete = 'true', date_complete = '{now}' WHERE id = {row_id}"
        )
        self.db.get_connection().commit()

    def void_task(self, row_id):
        now = kronos.get_date_time_as_string()
        self.db.get_cursor().execute(
            f"UPDATE {self.table_name} SET is_void = 'true', date_complete = '{now}' WHERE id = {row_id}"
        )
        self.db.get_connection().commit()

    def get_overdue_tasks(self):
        rows = []
        for row in self.get_rows():
            date_set = row[3]
            days_to_complete = row[5]
            is_complete = row[6]
            if is_complete == "false":
                if kronos.is_overdue(date_set, days_to_complete):
                    rows.append(row)
        return rows

    def insert_task(self, task, days_to_complete):
        TasksFacade.increment_row_count()
        self.db.get_cursor().execute(
            "INSERT INTO {} ({}, {}, {}, {}, {}, {}, {}, {}) VALUES (?, ?, ?, ?, ?, ?, ?, ?)".format(
                self.table_name, *self.schema
            ),
            (
                TasksFacade.__rows_in_table,
                "TASK",
                task,
                kronos.get_date_time_as_string(),
                "TBD****************",
                days_to_complete,
                "false",
                "false",
            ),
        )
        self.db.get_connection().commit()

    def check_if_not_completed(self, task_id):
        cursor = self.db.get_cursor()
        cursor.execute(
            f"SELECT is_complete from {self.table_name} WHERE id = {task_id}"
        )
        record = cursor.fetchall()
        is_complete = record[0][0]

        if is_complete == "true":
            return 0
        else:
            return 1
    def check_if_not_voided(self, task_id):
        cursor = self.db.get_cursor()
        cursor.execute(
            f"SELECT is_void from {self.table_name} WHERE id = {task_id}"
        )
        record = cursor.fetchall()
        is_complete = record[0][0]

        if is_complete == "true":
            return 0
        else:
            return 1

    @classmethod
    def reset_row_count(cls):
        TasksFacade.__rows_in_table = 0

    @classmethod
    def increment_row_count(cls):
        TasksFacade.__rows_in_table = TasksFacade.__rows_in_table + 1
