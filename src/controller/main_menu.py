from errors.custom_exceptions import InvalidOptionError
from view.menus import print_header
from services.auth_service import signup, login
from services.user_service import start_user_menu
from utils.utilities import cls

options = {
    "LOGIN": 1,
    "SIGNUP": 2,
    "EXIT": 0
}


def handle_main_menu(option: int):

    if option == options['LOGIN']:
        login()

    elif option == options['SIGNUP']:
        signup()

    elif option == options['EXIT']:
        print('Hasta pronto...')

    else:
        raise InvalidOptionError
