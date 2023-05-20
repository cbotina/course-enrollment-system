from model.models import Course
from session.session_data import SessionData
from datasource import course_repository
from view.menus import print_header, print_course_menu
from errors.custom_exceptions import InvalidOptionError, NotFoundError
from utils.utilities import cls
from controller.course_menu import handle_course_menu


def create_course():
    print_header('CREAR CURSO')

    name = input("Ingrese el nombre del curso: ")
    price = int(input("Ingrese el precio del curso: "))
    teacher_id = SessionData().get_user().id

    new_course = Course(0, name, teacher_id, price)

    course_repository.save(new_course)

    print("Curso creado exitosamente")


def set_session_course(course_id: int):
    course = course_repository.find_one_by_id(course_id)
    SessionData().set_course(course)


def start_course_menu():
    course = SessionData().get_course()
    print_header(f'CURSO {course.name}')
    option = 1
    while option != 0:
        try:
            cls()
            print_course_menu(course.name)
            option = int(input())
            cls()
            handle_course_menu(option)

        except Exception:
            print("errorsito")


def start_courses_menu():

    print_header('MIS CURSOS')
    option = 1
    teacher_id = SessionData().get_user().id
    courses = course_repository.find_by_teacher_id(int(teacher_id))
    while option != 0:
        try:
            for course in courses:
                print(course)
            print("0. Salir\n")
            option = int(input())
            if option == 0:
                break
            set_session_course(option)
            start_course_menu()

        except InvalidOptionError:
            print(f'\nERROR: El curso # {option} no existe')
        except ValueError:
            print('\nERROR: La opcion debe ser un numero')
        except NotFoundError:
            print(f'\nERROR: El curso # {option} no existe')
