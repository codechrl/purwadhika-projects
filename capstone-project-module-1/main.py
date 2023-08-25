import os
from copy import deepcopy

from data import (
    TABLE_INDEX,
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
    print("====================================================")
    print(
        """
   ___                          ____   _ __       
  / _ \__ _______    _____ ____/ / /  (_) /_____ _
 / ___/ // / __/ |/|/ / _ `/ _  / _ \/ /  '_/ _ `/
/_/   \_,_/_/  |__,__/\_,_/\_,_/_//_/_/_/\_\\_,_/ 
               ______                             
              / __/ /____  _______                
             _\ \/ __/ _ \/ __/ -_)               
          __/___/\__/\___/_/  \__/                
         / __/_ _____ / /____ __ _                
        _\ \/ // (_-</ __/ -_)  ' \               
       /___/\_, /___/\__/\__/_/_/_/               
           /___/                                  
"""
    )
    print("====================================================")


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
    print("2. Update ")
    print("3. Delete ")
    print()
    print("0. Back")

    print()
    user_input = input("Go To: ")

    if user_input == "1":
        insert_row(table_idx)
    elif user_input == "2":
        update_row(table_idx)
    elif user_input == "3":
        delete_row(table_idx)
    else:
        pass


def insert_row(table_idx):
    clear_console()
    print(TABLE_INDEX[table_idx].upper())

    data = get_data(TABLE_INDEX[table_idx])
    print_table(data)
    print()
    print("Input Row Values")
    print()
    new_row = {}
    for k, v in data[0].items():
        input_row = input(f"{k}: ")
        new_row[k] = input_row

    clear_console()

    print_table([new_row])
    print()
    user_input = input("Are You Sure to Insert This Row (y/n): ")
    if user_input.lower() == "y":
        insert_data(TABLE_INDEX[table_idx], new_row)
    see_data(table_idx)


def update_row(table_idx, msg_not_found=False):
    new_row = {}
    clear_console()
    print(TABLE_INDEX[table_idx].upper())

    data = get_data(TABLE_INDEX[table_idx])
    print_table(data)
    print()
    print("0. Back")
    if msg_not_found:
        print("\nID not Found")
    print()
    user_input_id = input("Input ID to Update: ")

    if user_input_id == "0":
        see_data(table_idx)
    elif user_input_id in [row.get("id") for row in data]:
        new_row = {}
        print()
        print("Input Update Values")
        print()

        clear_console()

        old_row = deepcopy([row for row in data if row.get("id") == user_input_id])
        old_row[0]["update"] = "old"
        new_row = deepcopy(old_row[0])
        new_row["update"] = "new"

        while True:
            clear_console()
            print_table(old_row + [new_row])
            print()
            user_input = input("Enter Column Name ('!done' to complete updating): ")
            if user_input == "!done":
                break

            if user_input.lower() in data[0].keys() and user_input.lower() != "id":
                col_value = input(f"{user_input}: ")
                new_row[user_input] = col_value

        user_input = input("Are You Sure to Update This Row (y/n): ")
        if user_input.lower() == "y":
            print(new_row)
            del new_row["update"]
            update_data(TABLE_INDEX[table_idx], new_row)
        see_data(table_idx)

    else:
        update_row(table_idx, True)


def delete_row(table_idx, msg_not_found=False):
    clear_console()
    print(TABLE_INDEX[table_idx].upper())

    data_table = get_data(TABLE_INDEX[table_idx])
    print_table(data_table)

    print()
    print("0. Back")
    if msg_not_found:
        print("\nID not Found")
    print()
    user_input = input("Input ID to Delete: ")
    if user_input == "0":
        see_data(table_idx)
    elif user_input in [row.get("id") for row in data_table]:
        clear_console()
        deleted_row = [row for row in data_table if row.get("id") == user_input]

        print(TABLE_INDEX[table_idx].upper())
        print_table(deleted_row)
        print()
        user_input = input("Are You Sure to Delete This Row (y/n): ")

        if user_input.lower() == "y":
            delete_data(TABLE_INDEX[table_idx], deleted_row[0])
            see_data(table_idx)
    else:
        delete_row(table_idx, msg_not_found=True)


while True:
    banner()
    main_menu()
