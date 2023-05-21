from datasource import course_repository
from datasource import bill_repository
from model.models import Bill
from session.session_data import SessionData
from view.menus import print_header


def enroll_course():
    print_header('MATRICULAR CURSO')
    course_id = int(input("Ingrese el id del curso a matricular: "))
    course = course_repository.find_one_by_id(course_id)
    user = SessionData().get_user()
    bill = Bill(0, user.id, course.id)
    bill_repository.save(bill)
    print("Curso matriculado exitosamente")
