import functools
import interface_common
import os
import textwrap


class InterfaceAnalytics:
    __menu = """
        0: Return to MODE
        1: Print metrics
        2: Quit
        """

    def __init__(self, notes_facade, tasks_facade):
        self.notes_facade = notes_facade
        self.tasks_facade = tasks_facade
        self.__menu_map = {
            "0": interface_common.to_previous_menu,
            "1": interface_common.clear_screen,
            "2": functools.partial(interface_common.quit_program, self.notes_facade),
        }

    def prompt_analytics(self):
        banner = os.path.join(os.path.dirname(__file__), "banners/lytics.txt")
        interface_common.print_ascii_banner(interface_common.parse_ascii_banner(banner))
        return input(textwrap.dedent(InterfaceAnalytics.__menu))

    def run_menu_loop_analytics(self):
        while True:
            choice = self.prompt_analytics()
            interface_common.map_choice_to_function(self.__menu_map, choice)
