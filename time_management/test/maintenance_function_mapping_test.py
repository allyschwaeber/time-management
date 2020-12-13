import unittest
import sqlitedb
import interface_maintenance
import interface_mode
import os
import ddl
import interface_common
import functools


class MaintenanceFunctionMappingTest(unittest.TestCase):

    def init(self):

        self.db_v1 = sqlitedb.SQLiteDatabase(
                        os.path.join(os.path.dirname(__file__), "TM_v1.db")
                    )

        # Scan for and create tables
        self.data_def = ddl.DataDefinitionLanguage(self.db_v1)
        self.data_def.create_all_tables()

        self.mode = interface_mode.InterfaceMode(self.db_v1)
        self.maint = interface_maintenance.InterfaceMaintenance(
                        self.mode.notes_facade,
                        self.mode.tasks_facade,
                        self.data_def
                    )
        self.__menu_map = self.maint._InterfaceMaintenance__menu_map

    def test_check_map(self):
        self.init()
        self.assertEqual(len(self.__menu_map), 3)
        self.assertIsInstance(self.__menu_map, dict)
        k = 0
        for i in self.__menu_map.keys():
            self.assertEqual(i, str(k))
            k += 1
        self.assertEqual(
                self.__menu_map["0"], interface_common.to_previous_menu
            )

        self.assertEqual(
                self.__menu_map["1"], self.maint.delete_history
            )

        self.assertEqual(
                type(self.__menu_map["2"]),
                type(
                    functools.partial(
                        interface_common.quit_program,
                        self.maint.notes_facade
                    )
                )
            )
        self.assertEqual(
                self.__menu_map["2"].func,
                functools.partial(
                    interface_common.quit_program,
                    self.maint.notes_facade
                ).func
            )
        self.assertEqual(
                self.__menu_map["2"].args,
                functools.partial(
                    interface_common.quit_program,
                    self.maint.notes_facade
                ).args
            )
        self.assertEqual(
                self.__menu_map["2"].keywords,
                functools.partial(
                    interface_common.quit_program,
                    self.maint.notes_facade
                ).keywords
            )


if __name__ == "__main__":
    unittest.main()
