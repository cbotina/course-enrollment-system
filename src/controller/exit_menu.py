from errors.custom_exceptions import InvalidOptionError

options = {
    "EXIT": 0,
}


def handle_course_menu(option: int):

    if option == options['EXIT']:
        print('Saliendo...')

    else:
        raise InvalidOptionError
