from utils.initializers import create_tables
from utils.utilities import cls
from view.menus import print_main_menu, print_header
from controller.main_menu import handle_main_menu
from errors.custom_exceptions import *


create_tables()
cls()
print_header('BIENVENIDO')

option = 1

while option != 0:

    try:
        input("Presione enter para continuar\n\n")
        cls()
        print_main_menu()
        option = int(input())
        cls()
        handle_main_menu(option)

    except InvalidOptionError:
        print('\nERROR: La opcion no existe')

    except ValueError:
        print('\nERROR: La opcion debe ser un numero')

    except UserNotFoundError:
        print('\nERROR: Credenciales incorrectas')

    except BadCredentialsError:
        print('\nERROR: Credenciales incorrectas')
