from errors.custom_exceptions import InvalidOptionError
from view.menus import print_header
from services.exit_service import ask_exit
from services.reports_service import show_course_details, show_course_students

options = {
    "COURSE_DETAILS": 1,
    "ENRROLLED_STUDENTS": 2,
    "EXIT": 0
}


def handle_course_menu(option: int):

    if option == options['COURSE_DETAILS']:
        show_course_details()
        ask_exit()

    elif option == options['ENRROLLED_STUDENTS']:
        show_course_students()
        ask_exit()

    elif option == options['EXIT']:
        pass

    else:
        raise InvalidOptionError
