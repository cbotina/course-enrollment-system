from errors.custom_exceptions import InvalidOptionError
from view.menus import print_header
from services.auth_service import signup, login
from session.session_data import SessionData


options = {
    "LOGIN": 1,
    "SIGNUP": 2,
    "EXIT": 0
}


def handle_main_menu(option: int):

    if option == options['LOGIN']:
        print_header('INICIO DE SESION')
        login()
        print(SessionData().get_user())

    elif option == options['SIGNUP']:
        print_header('REGISTRO DE USUARIOS')
        signup()

    elif option == options['EXIT']:
        print('Hasta pronto...')

    else:
        raise InvalidOptionError
