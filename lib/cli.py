#!/usr/bin/env python3.12
import helpers

def menu():
    while True:
        print('0.\tQuit')
        print('1.\tView all libraries')
        selection = input('Select from the following menu: ')

        try:
            selection = int(selection)
        except ValueError:
            print('Invalid input, please enter a number.')
            continue  # Ask for input again

        match selection:
            case 0:
                helpers.exit_program()
                break  # Exit the loop
            case 1:
                helpers.show_all_departments()
            case _:
                print('Invalid choice')

if __name__ == "__main__":
    # init_db()
    menu()


