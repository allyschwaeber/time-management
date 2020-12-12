import unittest
import sqlitedb
import facade_notes
import interface_mode
import os
import facade_tasks
import kronos
import getpass
import ddl
import speech_cadence_emulator
import interface_common
import functools

class ModeFunctionMappingTest(unittest.TestCase):
    def setup_db(self):
        db_v1 = sqlitedb.SQLiteDatabase(os.path.join(os.path.dirname(__file__), "TM_v1.db"))

        # Scan for and create tables
        data_def = ddl.DataDefinitionLanguage(db_v1)
        data_def.create_all_tables()

        return db_v1

    
    def init(self):
        self.db_v1 = self.setup_db()
        self.mode = interface_mode.InterfaceMode(self.db_v1)
        self.__menu_map = self.mode._InterfaceMode__menu_map
    
    def test_check_map(self):
        self.init()
        self.assertEqual(len(self.__menu_map), 4)
        self.assertIsInstance(self.__menu_map, dict)
        k = 1
        for i in self.__menu_map.keys():
            self.assertEqual(i,str(k))
            k += 1
        self.assertEqual(self.__menu_map["1"], self.mode.start_tm_menu_loop)

        self.assertEqual(self.__menu_map["2"], self.mode.start_lytics_menu_loop)

        self.assertEqual(self.__menu_map["3"], self.mode.start_maint_menu_loop)

        self.assertEqual(type(self.__menu_map["4"]),type(functools.partial(interface_common.quit_program,self.mode.notes_facade)))
        self.assertEqual(self.__menu_map["4"].func,functools.partial(interface_common.quit_program,self.mode.notes_facade).func)
        self.assertEqual(self.__menu_map["4"].args,functools.partial(interface_common.quit_program,self.mode.notes_facade).args)
        self.assertEqual(self.__menu_map["4"].keywords,functools.partial(interface_common.quit_program,self.mode.notes_facade).keywords)


if __name__ == "__main__":
    unittest.main()
