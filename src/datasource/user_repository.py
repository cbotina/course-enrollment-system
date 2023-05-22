from model.models import User
from config.database import DbConnection
from errors.custom_exceptions import NotFoundError
from . import teacher_repository
from . import student_repository


conn = DbConnection().get_connection()


def find_one_by_email(email: str) -> User:
    teachers = teacher_repository.find_all()
    students = student_repository.find_all()
    users = teachers+students
    matches = list(filter(lambda u: u.email == email, users))
    if len(matches) == 0:
        raise NotFoundError
    else:
        return matches[0]
