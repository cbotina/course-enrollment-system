from errors.custom_exceptions import InvalidOptionError, BadCredentialsError
from datasource import student_repository, teacher_repository, user_repository
from model.models import Student, Teacher
from services.password_service import hash_password, check_password
from session.session_data import SessionData


def signup():
    name = input("Ingrese su nombre: ")
    email = input("Ingrese su correo: ")
    password = hash_password(input("Ingrese su contrasenia: "))
    role = int(input("Seleccione su rol( 1. Estudiante 2. Docente ): "))
    if (role == 1):
        new_student = Student(0, name, email, password)
        student_repository.save(new_student)
    elif (role == 2):
        speciality = input("Ingrese su especialidad: ")
        new_teacher = Teacher(0, name, email, password, speciality)
        teacher_repository.save(new_teacher)
    else:
        raise InvalidOptionError

    print('Registro exitoso')


def login():
    email = input("Ingrese su email: ")
    password = input("Ingrese su contrasenia: ")
    user = user_repository.find_one_by_email(email)
    if (not check_password(password, user.password)):
        raise BadCredentialsError
    SessionData().set_user(user)
