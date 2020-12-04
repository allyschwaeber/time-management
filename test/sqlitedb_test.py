import sqlitedb
import unittest


class SQLiteDBTest(unittest.TestCase):
    def setUp(self) -> None:
        self.db = sqlitedb.SQLiteDatabase()

    def tearDown(self) -> None:
        self.db.disconnect()

    def test_db_name(self):
        self.assertEqual(":memory:", self.db.get_db_name())
