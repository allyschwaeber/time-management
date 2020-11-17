import interface_common
import os
import textwrap
import functools
import threading
import ddl
import speech_cadence_emulator
import time
import random


class InterfaceStudy:
    __menu = """
        0: Return to MODE
        1: Quit
        """

    def __init__(self, notes_facade):
        self.notes_facade = notes_facade
        self.__menu_map = {
            "0": interface_common.to_previous_menu,
            "1": functools.partial(interface_common.quit_program, self.notes_facade),
        }

    # TODO :: KILL THREAD ON KEY INPUT
    def prompt_study(self):
        threading.Timer(2.5, self.print_glossary).start()
        banner = os.path.join(os.path.dirname(__file__), "banners/study.txt")
        interface_common.print_ascii_banner(interface_common.parse_ascii_banner(banner))
        return input(textwrap.dedent(InterfaceStudy.__menu))

    def run_menu_loop_study(self):
        while True:
            choice = self.prompt_study()
            interface_common.map_choice_to_function(self.__menu_map, choice)

    def print_glossary(self):
        glossary = ddl.DataDefinitionLanguage.parse_json(
            os.path.join(os.path.dirname(__file__), "knowledge_base/glossary.json")
        )
        random.shuffle(glossary)
        for entry in glossary:
            for term, definition in entry.items():
                speech_cadence_emulator.emulate_speech_cadence("\n\n" + term + ":")
                speech_cadence_emulator.emulate_speech_cadence(" " + definition)
                time.sleep(30)
