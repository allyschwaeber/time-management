import interface_mode
import facade_tasks
import kronos
import os
import getpass
import ddl
import sqlitedb
import speech_cadence_emulator


def main():
    on_startup()


def on_startup():
    # Initialize database
    db_v1 = sqlitedb.SQLiteDatabase(os.path.join(os.path.dirname(__file__), "TM_v1.db"))

    # Scan for and create tables
    data_def = ddl.DataDefinitionLanguage(db_v1)
    data_def.create_all_tables()

    # Create launch message
    tasks_facade = facade_tasks.TasksFacade(db_v1)
    time_of_day = kronos.get_time_of_day()
    user = getpass.getuser()
    number_of_overdue_items = len(tasks_facade.get_overdue_tasks())
    welcome_statement = f"\nGood {time_of_day} {user}. You have {number_of_overdue_items} overdue items.\n"
    #speech_cadence_emulator.emulate_speech_cadence(welcome_statement)

    # Launch MODE interface
    mode = interface_mode.InterfaceMode(db_v1)
    mode.run_menu_loop_mode()


if __name__ == "__main__":
    main()
