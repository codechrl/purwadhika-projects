import os

from data import (
    TABLE_INDEX,
    TABLE_PATHS,
    delete_data,
    get_data,
    insert_data,
    print_table,
    update_data,
)

RUN = True


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def banner():
    print("==========================")
    print("""PURWADHIKA\n            STORE\n                   SYSTEM""")
    print("==========================")


def main_menu_():
    clear_console()
    print("Menu")
    print("1. See Data")
    return input("Go To: ")


def main_menu():
    global RUN
    clear_console()
    banner()
    print()

    print("1. Store Data")
    print("2. Product Data")
    print("3. Transaction Data")

    print()
    user_input = input("Go To: ")

    see_data(user_input)


def see_data(table_idx):
    clear_console()
    print(TABLE_INDEX[table_idx].upper())

    data = get_data(TABLE_INDEX[table_idx])
    print_table(data)
    print()

    print("1. Insert ")
    print("2. Uodate ")
    print("3. Delete ")
    print("0. Back to Main Menu ")

    print()
    user_input = input("Go To: ")

    if user_input == "3":
        delete_row(table_idx)
    else:
        pass


def insert_row(table_idx):
    clear_console()
    print(TABLE_INDEX[table_idx].upper())

    data = get_data(TABLE_INDEX[table_idx])
    print_table(data)


def update_row(table_idx):
    clear_console()
    print(TABLE_INDEX[table_idx].upper())

    data = get_data(TABLE_INDEX[table_idx])
    print_table(data)

    print()
    user_input = input("Input ID to Delete: ")


def delete_row(table_idx):
    clear_console()
    print(TABLE_INDEX[table_idx].upper())

    data_table = get_data(TABLE_INDEX[table_idx])
    print_table(data_table)

    print()
    user_input = input("Input ID to Delete: ")

    clear_console()
    deleted_row = [row for row in data_table if row.get("id") == user_input]
    print(TABLE_INDEX[table_idx].upper())
    print_table(deleted_row)
    print()
    user_input = input("Are You Sure Delete This Row (y/n): ")

    if user_input.lower() == "y":
        delete_data(TABLE_INDEX[table_idx], deleted_row[0])
        see_data(table_idx)

    else:
        see_data(table_idx)


while RUN:
    banner()
    main_menu()
