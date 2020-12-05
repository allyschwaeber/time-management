import unittest
import sqlitedb
import facade_notes
import ddl
import dml


class NotesFacadeTest(unittest.TestCase):
    def setUp(self) -> None:
        self.db = sqlitedb.SQLiteDatabase()
        self.data_def = ddl.DataDefinitionLanguage(self.db)
        self.data_man = dml.DataManipulationLanguage(self.db)
        self.data_def.create_table(
            "notes",
            ddl.DataDefinitionLanguage.parse_json(
                "time_management/table_schemas/notes.json"
            ),
        )
        self.notes_facade = facade_notes.NotesFacade(self.db)
        self.notes_facade.insert_note("THIS IS A NOTE")

    def tearDown(self) -> None:
        self.db.disconnect()

    def test_count_rows(self):
        self.assertEqual(1, self.notes_facade.count_rows())

    def test_get_rows(self):
        rows = self.notes_facade.get_rows()
        row_index = 0
        note_index = 2
        self.assertEqual("THIS IS A NOTE", rows[row_index][note_index])
