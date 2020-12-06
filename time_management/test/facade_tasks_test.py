import unittest
import sqlitedb
import facade_tasks
import ddl
import dml


class NotesFacadeTest(unittest.TestCase):
    def setUp(self) -> None:
        self.db = sqlitedb.SQLiteDatabase()
        self.data_def = ddl.DataDefinitionLanguage(self.db)
        self.data_man = dml.DataManipulationLanguage(self.db)
        self.data_def.create_table(
            "tasks",
            ddl.DataDefinitionLanguage.parse_json(
                "time_management/table_schemas/tasks.json"
            ),
        )
        self.notes_facade = facade_tasks.TasksFacade(self.db)
        self.notes_facade.insert_task("DO THIS", 1)
        self.notes_facade.insert_task("DO THAT", 2)

    def tearDown(self) -> None:
        self.db.disconnect()

    def test_count_rows(self):
        self.assertEqual(2, self.notes_facade.count_rows())

    def test_get_ids(self):
        self.assertTrue(1 in self.notes_facade.get_ids())

    def test_get_rows(self):
        rows = self.notes_facade.get_rows()
        row_index = 0
        task_index = 2
        self.assertEqual("DO THIS", rows[row_index][task_index])

    def test_get_overdue_tasks(self):
        self.assertEqual(0, len(self.notes_facade.get_overdue_tasks()))

    def test_complete_task(self):
        self.notes_facade.complete_task(2)
        rows = self.notes_facade.get_rows()
        row_index = 1
        is_complete_index = 6
        self.assertEqual("true", rows[row_index][is_complete_index])
