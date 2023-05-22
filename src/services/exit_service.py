from view.menus import print_exit_menu
from controller.exit_menu import handle_exit_menu
from utils.utilities import cls
from errors.custom_exceptions import InvalidOptionError


def ask_exit():
    print_exit_menu()
    option = 1
    while option != 0:
        try:
            option = int(input())
            handle_exit_menu(option)
        except InvalidOptionError:
            print(f'\nERROR: La opcion {option} no existe')
        except ValueError:
            print('\nERROR: La opcion debe ser un numero')
