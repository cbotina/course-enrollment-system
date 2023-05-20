from view.menus import print_student_menu
from utils.utilities import cls
from controller.student_menu import handle_student_menu


def start_student_menu(name: str):

    option = 1

    while option != 0:
        cls()
        print_student_menu(name)
        option = int(input())
        cls()
        handle_student_menu(option)
