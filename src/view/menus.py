def print_header(title: str):
    print(f'\n====={title}=====\n')


def print_exit_menu():
    print('''

    0. Salir

    ''')


def print_main_menu():
    print_header('MENU PRINCIPAL')
    print('''
    Seleccione una opcion:

    1. Iniciar Sesion
    2. Registrarse
    0. Salir del programa

    ''')


def print_student_menu(name: str):
    print_header(f'BIENVENIDO {name.upper()}')
    print('''
    Seleccione una opcion:

    1. Ver Cursos
    2. Matricularse a Curso
    0. Cerrar Sesion

    ''')


def print_teacher_menu(name: str):
    print_header(f'BIENVENIDO {name.upper()}')
    print('''
    Seleccione una opcion:

    1. Crear Curso
    2. Mis Cursos
    0. Cerrar Sesion
    
    ''')


def print_courses_menu(courses: list):
    print('''
    Seleccione un curso por ID:
    
    ''')
    options = ''
    for course in courses:
        options = options + course + '\n'
    print(options+'0. Salir \n')


def print_course_menu(course_name):
    print_header(f'CURSO {course_name.upper()}')
    print('''
    Seleccione una opcion:

    1. Detalles del curso
    2. Estudiantes Matriculados
    0. Salir
    
    ''')


def print_exit_menu():
    print('''
    
    0. Salir

    ''')
