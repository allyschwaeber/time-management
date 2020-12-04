import unittest
import sqlitedb
import ddl
import interface_time_management
import facade_notes
import facade_tasks


class TimeManagementTest(unittest.TestCase):
    def setUp(self) -> None:
        self.db = sqlitedb.SQLiteDatabase()
        self.data_def = ddl.DataDefinitionLanguage(self.db)
        self.data_def.create_table(
            "tasks",
            ddl.DataDefinitionLanguage.parse_json(
                "time_management/table_schemas/tasks.json"
            ),
        )
        self.data_def.create_table(
            "notes",
            ddl.DataDefinitionLanguage.parse_json(
                "time_management/table_schemas/notes.json"
            ),
        )
        self.notes_facade = facade_notes.NotesFacade(self.db)
        self.tasks_facade = facade_tasks.TasksFacade(self.db)
        self.tasks_facade.insert_task("DO THIS", 1)
        self.notes_facade.insert_note("A NOTE")
        self.interface_tm = interface_time_management.InterfaceTM(
            self.notes_facade, self.tasks_facade, self.db
        )

    def tearDown(self) -> None:
        self.db.disconnect()

    # This method currently sits on the InterfaceTM class, but it could eventually
    # be re-factored to a helper/validator class.
    def test_validates_id_works_as_expected(self):
        ids = [1, 2, 3, 4]

        invalid1 = "one"
        invalid2 = "o32o"
        self.assertFalse(
            interface_time_management.InterfaceTM.are_valid_tasks(invalid1, ids)
        )
        self.assertFalse(
            interface_time_management.InterfaceTM.are_valid_tasks(invalid2, ids)
        )

        valid1 = "1"
        valid2 = "2"
        self.assertTrue(
            interface_time_management.InterfaceTM.are_valid_tasks(valid1, ids)
        )
        self.assertTrue(
            interface_time_management.InterfaceTM.are_valid_tasks(valid2, ids)
        )

    def test_print_scrum_notes(self):
        pass
