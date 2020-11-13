import interface_common
import facade_tasks
import facade_notes
import os
import textwrap
import functools


class InterfaceMaintenance:
    __menu = """
        0: Return to MODE
        1: Delete history
        2: Quit
        """

    def __init__(self, notes_facade, tasks_facade, data_def):
        self.notes_facade = notes_facade
        self.tasks_facade = tasks_facade
        self.data_def = data_def
        self.__menu_map = {
            "0": interface_common.to_previous_menu,
            "1": self.delete_history,
            "2": functools.partial(interface_common.quit_program, self.notes_facade),
        }

    def prompt_maintenance(self):
        banner = os.path.join(os.path.dirname(__file__), "banners/maint.txt")
        interface_common.print_ascii_banner(interface_common.parse_ascii_banner(banner))
        return input(textwrap.dedent(InterfaceMaintenance.__menu))

    def run_menu_loop_maintenance(self):
        while True:
            choice = self.prompt_maintenance()
            interface_common.map_choice_to_function(self.__menu_map, choice)

    def delete_history(self):
        interface_common.clear_screen()
        choice = input(
            "Are you sure you want to delete your history?\nSubmit 'y' to drop table\nSubmit 'n' to return to maintenance\n"
        )
        if choice == "y":
            print("\nDeleting history...\n\n")
            self.notes_facade.delete_history()
            facade_notes.NotesFacade.reset_row_count()
            self.tasks_facade.delete_history()
            facade_tasks.TasksFacade.reset_row_count()
            self.data_def.create_all_tables()
        elif choice == "n":
            self.run_menu_loop_maintenance()
