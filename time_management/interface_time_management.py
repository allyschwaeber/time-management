import interface_common
import format_decorators
import os
import textwrap
import functools
import time


class InterfaceTM:
    __menu = """
        0: Return to MODE
        1: Make a note
        2: Set a task
        3: Print notes
        4: Print tasks
        5: Complete tasks
        6: Print overdue
        7: Print SCRUM notes
        8: Quit
        """

    def __init__(self, notes_facade, tasks_facade, dml):
        self.notes_facade = notes_facade
        self.tasks_facade = tasks_facade
        self.dml = dml
        self.__menu_map = {
            "0": interface_common.to_previous_menu,
            "1": self.__make_a_note,
            "2": self.__set_a_task,
            "3": self.__print_notes,
            "4": self.__print_tasks,
            "5": self.__complete_task,
            "6": self.__print_overdue,
            "7": self.__print_scrum_notes,
            "8": functools.partial(interface_common.quit_program, self.notes_facade),
        }

    def run_menu_loop_tm(self):
        while True:
            choice = self.__prompt_time_management()
            interface_common.map_choice_to_function(self.__menu_map, choice)

    def __prompt_time_management(self):
        banner = os.path.join(os.path.dirname(__file__), "banners/tm.txt")
        interface_common.print_ascii_banner(interface_common.parse_ascii_banner(banner))
        return input(textwrap.dedent(InterfaceTM.__menu))

    def __make_a_note(self):
        interface_common.clear_screen()
        print("0 to cancel\n")
        note = input("Make a note: ")
        if note == "0":
            interface_common.clear_screen()
            self.run_menu_loop_tm()
        else:
            self.notes_facade.insert_note(note)
            interface_common.clear_screen()

    def __set_a_task(self):
        interface_common.clear_screen()
        print("0 to cancel\n")
        note = input("Set a task: ")
        if note == "0":
            interface_common.clear_screen()
            self.run_menu_loop_tm()
        else:
            days_to_complete = input("Set number of days to complete: ")
            try:
                float(days_to_complete)
                self.tasks_facade.insert_task(note, days_to_complete)
            except ValueError:
                print("You need to enter a valid number of days!")
                print("Press any key to continue...", end="")
                input()
                self.__set_a_task()
            interface_common.clear_screen()

    def __print_notes(self):
        interface_common.clear_screen()
        note_rows = self.notes_facade.get_rows()
        formatted_notes = format_decorators.format_note(note_rows)
        InterfaceTM.__print_entries(formatted_notes)

    def __print_tasks(self):
        interface_common.clear_screen()
        task_rows = self.tasks_facade.get_rows()
        formatted_tasks = format_decorators.format_task(task_rows)
        InterfaceTM.__print_entries(formatted_tasks)

    @staticmethod
    def __print_entries(entries):
        if entries:
            for entry in entries:
                print(entry)
            print(2 * "\n")

    def __complete_task(self, first_run=True):
        interface_common.clear_screen()
        print("0 to cancel\n")
        if first_run:
            task_input = input("Enter space delimited task IDs for completion: ")
        else:
            task_input = input("One or more task IDs not found. Please try again: ")

        task_ids = self.__split_tasks(task_input)

        if task_ids[0] == "0":
            interface_common.clear_screen()
            self.run_menu_loop_tm()
        elif InterfaceTM.are_valid_tasks(task_ids, self.tasks_facade.get_ids()):
            for task_id in task_ids:
                if self.tasks_facade.check_if_not_completed(task_id):
                    task = self.dml.arbitrary_select("task", "tasks", f"id = {task_id}")[0][0]
                    self.tasks_facade.complete_task(task_id)
                    self.notes_facade.insert_note("Completed Task " + task_id + ": " + task)
                else:
                    print(f"You have already completed this task with task id - {task_id}")
                    print("please wait !!")
                    time.sleep(3)
                    self.__complete_task(False)

            interface_common.clear_screen()
        else:
            self.__complete_task(False)

    @staticmethod
    def are_valid_tasks(tasks_to_complete, valid_task_ids):
        valid_tasks = []
        invalid_tasks = []
        for task_id in tasks_to_complete:
            if task_id.isdigit() and (int(task_id) in valid_task_ids):
                valid_tasks.append(task_id)
            else:
                invalid_tasks.append(task_id)
        if invalid_tasks:
            return False
        else:
            return True

    def __split_tasks(self, input_tasks):
        return input_tasks.split()

    def __print_overdue(self):
        interface_common.clear_screen()
        task_rows = self.tasks_facade.get_overdue_tasks()
        formatted_tasks = format_decorators.format_task(task_rows)
        for task in formatted_tasks:
            print(task)

    def __print_scrum_notes(self):
        interface_common.clear_screen()
        banner = os.path.join(os.path.dirname(__file__), "banners/scrum.txt")
        interface_common.print_ascii_banner(interface_common.parse_ascii_banner(banner))
        note_rows = self.notes_facade.get_last_workday()
        formatted_notes = format_decorators.format_note(note_rows)
        task_rows = self.tasks_facade.get_last_workday()
        formatted_tasks = format_decorators.format_task(task_rows)
        all_items = formatted_notes + list("\n") + formatted_tasks
        InterfaceTM.__print_entries(all_items)
