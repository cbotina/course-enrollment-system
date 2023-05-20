from errors.custom_exceptions import InvalidOptionError
from view.menus import print_header

options = {
    "LOGIN": 1,
    "SIGNUP": 2,
    "EXIT": 0
}


def handle_main_menu(option: int):

    if option == options['LOGIN']:
        print_header('INICIO DE SESION')

    elif option == options['SIGNUP']:
        print_header('REGISTRO DE USUARIOS')

    elif option == options['EXIT']:
        print('Saliendo del programa...')

    else:
        raise InvalidOptionError
