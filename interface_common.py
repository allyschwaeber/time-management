import os

menu_cache = []


def parse_ascii_banner(file):
    f = open(file, "r")
    lines = f.readlines()
    f.close()
    return lines


def print_ascii_banner(lines):
    for line in lines:
        print(line.rstrip("\n"))
    print("\n")


def clear_screen():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")


def quit_program(facade):
    clear_screen()
    facade.disconnect()
    quit()


def initialize_menu(menu_loop, is_startup=False):
    if not is_startup:
        clear_screen()
    menu_cache.append(menu_loop)


def to_previous_menu():
    clear_screen()
    menu_cache[-2]()


def map_choice_to_function(menu_map, choice):
    action = menu_map.get(choice)
    if action:
        action()
    else:
        clear_screen()
        print("Choice not recognized.")


def print_cancel_option():
    print("0 to cancel\n")
