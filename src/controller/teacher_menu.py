from errors.custom_exceptions import InvalidOptionError
from view.menus import print_header

options = {
    "CREATE_COURSE": 1,
    "MY COURSES": 2,
    "EXIT": 0
}


def handle_student_menu(option: int):
    if option == options['SEARCH_COURSES']:
        print_header('CURSOS DISPONIBLES')

    elif option == options['ENROLL_COURSES']:
        print_header('MATRICULAR CURSO')

    elif option == options['TOP_UP_BALANCE']:
        print_header('RECARGAR SALDO')

    elif option == options['EXIT']:
        print('Saliendo del programa...')

    else:
        raise InvalidOptionError
