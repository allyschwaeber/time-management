import interface_common
import interface_time_management
import interface_maintenance
import interface_analytics
import facade_notes
import facade_tasks
import os
import textwrap
import ddl
import dml


class InterfaceMode:
    __menu = """
        1: Time management
        2: Analytics
        3: Maintenance
        4: Quit
        """

    def __init__(self, db):
        self.data_def = ddl.DataDefinitionLanguage(db)
        self.notes_facade = facade_notes.NotesFacade(db)
        self.tasks_facade = facade_tasks.TasksFacade(db)
        self.interface_tm = interface_time_management.InterfaceTM(
            self.notes_facade, self.tasks_facade, dml.DataManipulationLanguage(db)
        )
        self.interface_maint = interface_maintenance.InterfaceMaintenance(
            self.notes_facade, self.tasks_facade, self.data_def
        )
        self.interface_lytics = interface_analytics.InterfaceAnalytics(
            self.notes_facade, self.tasks_facade
        )

    def prompt_mode(self):
        interface_common.initialize_menu(self.run_menu_loop_mode, True)
        banner = os.path.join(os.path.dirname(__file__), "banners/mode.txt")
        interface_common.print_ascii_banner(interface_common.parse_ascii_banner(banner))
        return input(textwrap.dedent(InterfaceMode.__menu))

    def map_choice_to_function(self, choice):
        if choice == "1":
            interface_common.initialize_menu(self.interface_tm.run_menu_loop_tm)
            self.interface_tm.run_menu_loop_tm()
        elif choice == "2":
            interface_common.initialize_menu(
                self.interface_lytics.run_menu_loop_analytics
            )
            self.interface_lytics.run_menu_loop_analytics()
        elif choice == "3":
            interface_common.initialize_menu(
                self.interface_maint.run_menu_loop_maintenance
            )
            self.interface_maint.run_menu_loop_maintenance()
        elif choice == "4":
            interface_common.quit_program(self.notes_facade)
        else:
            print("Choice not recognized.")

    def run_menu_loop_mode(self):
        while True:
            choice = self.prompt_mode()
            self.map_choice_to_function(choice)