from config.database import DbConnection

conn = DbConnection().get_connection()


def get_courses_details():
    cursor = conn.cursor()
    cursor.execute('''
        select c.id, c.name, t.name from course c join teacher t
        on c.teacher_id = t.id
    ''')
    query_result = cursor.fetchall()
    result = map(
        lambda x: f'{x[0]}. Curso: {x[1]} | Docente: {x[2]}', query_result)
    return result


def get_course_details(course_id):
    cursor = conn.cursor()
    cursor.execute(
        f'select c.name, t.name from course c join teacher t on c.teacher_id = t.id where c.id = {course_id}')
    query_result = cursor.fetchall()
    result = query_result[0]
    course_details = f'Nombre del curso: {result[0].capitalize()} | Docente: {result[1]} '
    cursor.execute(f'select id from bill where course_id = {course_id}')
    result = cursor.fetchall()
    course_details = course_details + \
        f'\nEstudiantes Matriculados: {len(result)}'

    return course_details


def get_course_students(course_id):
    cursor = conn.cursor()
    cursor.execute(
        f'select s.name, s.email from bill b join student s on b.student_id = s.id where b.course_id = {course_id}')
    query_result = cursor.fetchall()
    result = map(
        lambda x: f'Nombre: {x[0]} | Correo: {x[1]}', query_result)
    return result
