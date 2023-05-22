from errors.custom_exceptions import InvalidOptionError
from controller.exit_menu import handle_exit_menu
from services.course_service import create_course, start_courses_menu
from datasource import course_repository
from services.exit_service import ask_exit

options = {
    "CREATE_COURSE": 1,
    "MY_COURSES": 2,
    "EXIT": 0
}


def handle_teacher_menu(option: int):
    if option == options['CREATE_COURSE']:
        create_course()
        ask_exit()

    elif option == options['MY_COURSES']:
        start_courses_menu()

    elif option == options['EXIT']:
        print('Cerrando Sesion...')

    else:
        raise InvalidOptionError
