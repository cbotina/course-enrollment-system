from errors.custom_exceptions import InvalidOptionError
from view.menus import print_header

options = {
    "COURSE_DETAILS": 1,
    "ENRROLLED_STUDENTS": 2
}


def handle_course_menu(option: int):

    if option == options['COURSE_DETAILS']:
        print_header('DETALLES DEL CURSO')

    elif option == options['ENRROLLED_STUDENTS']:
        print_header('ESTUDIANTES MATRICULADOS')

    else:
        raise InvalidOptionError
