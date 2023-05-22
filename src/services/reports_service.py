from session.session_data import SessionData
from view.menus import print_header
from datasource.reports import get_course_details, get_course_students


def show_course_details():
    course = SessionData().get_course()
    print_header(f'DETALLES DEL CURSO')
    print(get_course_details(course.id))


def show_course_students():
    course = SessionData().get_course()
    print_header(f'ESTUDIANTES MATRICULADOS')
    print(f'Curso: {course.name.capitalize()}\n')
    students = get_course_students(course.id)
    for student in students:
        print(student)
