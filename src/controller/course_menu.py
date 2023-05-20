from errors.custom_exceptions import InvalidOptionError
from view.menus import print_header
from services.exit_service import ask_exit

options = {
    "COURSE_DETAILS": 1,
    "ENRROLLED_STUDENTS": 2
}


def handle_course_menu(option: int):

    if option == options['COURSE_DETAILS']:
        print_header('DETALLES DEL CURSO')
        ask_exit()

    elif option == options['ENRROLLED_STUDENTS']:
        print_header('ESTUDIANTES MATRICULADOS')
        ask_exit()

    else:
        raise InvalidOptionError
