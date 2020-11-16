import functools
import interface_common
import interface_time_management
import interface_maintenance
import interface_analytics
import interface_study
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
        4: Study
        5: Quit
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
        self.interface_study = interface_study.InterfaceStudy(self.notes_facade)

        self.__menu_map = {
            "1": functools.partial(self.__run_tm, self.interface_tm.run_menu_loop_tm),
            "2": functools.partial(
                self.__run_analytics, self.interface_lytics.run_menu_loop_analytics
            ),
            "3": functools.partial(
                self.__run_maint, self.interface_maint.run_menu_loop_maintenance
            ),
            "4": functools.partial(
                self.__run_study, self.interface_study.run_menu_loop_study
            ),
            "5": functools.partial(interface_common.quit_program, self.notes_facade),
        }

    def prompt_mode(self):
        interface_common.initialize_menu(self.run_menu_loop_mode, True)
        banner = os.path.join(os.path.dirname(__file__), "banners/mode.txt")
        interface_common.print_ascii_banner(interface_common.parse_ascii_banner(banner))
        return input(textwrap.dedent(InterfaceMode.__menu))

    def __run_tm(self, run_menu_loop_tm):
        interface_common.initialize_menu(run_menu_loop_tm)
        self.interface_tm.run_menu_loop_tm()

    def __run_analytics(self, run_menu_loop_analytics):
        interface_common.initialize_menu(run_menu_loop_analytics)
        self.interface_lytics.run_menu_loop_analytics()

    def __run_maint(self, run_menu_loop_maint):
        interface_common.initialize_menu(run_menu_loop_maint)
        self.interface_maint.run_menu_loop_maintenance()

    def __run_study(self, run_menu_loop_study):
        interface_common.initialize_menu(run_menu_loop_study)
        self.interface_study.run_menu_loop_study()

    def run_menu_loop_mode(self):
        while True:
            choice = self.prompt_mode()
            interface_common.map_choice_to_function(self.__menu_map, choice)
