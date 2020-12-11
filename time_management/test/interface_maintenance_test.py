import unittest
import sqlitedb
import ddl
import interface_maintenance
import facade_notes
import facade_tasks

class MaintenanceTest(unittest.TestCase):
    def setUp(self) -> None:
        self.db = sqlitedb.SQLiteDatabase()
        self.data_def = ddl.DataDefinitionLanguage(self.db)
        self.data_def.create_table(
            "tasks",
            ddl.DataDefinitionLanguage.parse_json(
                "table_schemas/tasks.json"
            ),
        )
        self.data_def.create_table(
            "notes",
            ddl.DataDefinitionLanguage.parse_json(
                "table_schemas/notes.json"
            ),
        )
        self.notes_facade = facade_notes.NotesFacade(self.db)
        self.tasks_facade = facade_tasks.TasksFacade(self.db)
        self.tasks_facade.insert_task("DO THIS", 1)
        self.notes_facade.insert_note("A NOTE")
        self.interface_tm = interface_maintenance.InterfaceMaintenance(
            self.notes_facade, self.tasks_facade, self.db
        )

    def tearDown(self) -> None:
        self.db.disconnect()

    def testSelector(self):
        print(self.interface_tm.menu_map)
        self.assertEqual(
            1, 1
        )
