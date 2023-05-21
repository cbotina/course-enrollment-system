from view.menus import print_student_menu
from utils.utilities import cls
from controller.student_menu import handle_student_menu
from errors.custom_exceptions import CourseNotFoundError


def start_student_menu(name: str):

    option = 1
    while option != 0:
        try:
            cls()
            print_student_menu(name)
            option = int(input())
            cls()
            handle_student_menu(option)
        except CourseNotFoundError:
            print(f'\nERROR: El curso # {option} no existe')
            input("Presione enter para continuar\n\n")
        except ValueError:
            print(f'\nERROR: La opcion debe ser un numero')
            input("Presione enter para continuar\n\n")
