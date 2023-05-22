from view.menus import print_teacher_menu
from utils.utilities import cls
from controller.teacher_menu import handle_teacher_menu


def start_teacher_menu(name: str):

    option = 1

    while option != 0:
        try:
            cls()
            print_teacher_menu(name)
            option = int(input())
            cls()
            handle_teacher_menu(option)
        except Exception:
            print('error')
