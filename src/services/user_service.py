from session.session_data import SessionData
from model.models import Student, Teacher
from utils.utilities import cls
from services.student_service import start_student_menu
from services.teacher_service import start_teacher_menu
from view.menus import print_exit_menu
from controller.exit_menu import handle_exit_menu


def start_user_menu():
    user = SessionData().get_user()
    if (type(user) == Student):
        start_student_menu(user.name)
    elif (type(user) == Teacher):
        start_teacher_menu(user.name)
