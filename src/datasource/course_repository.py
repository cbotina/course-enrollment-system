from model.models import Course
from config.database import DbConnection
from errors.custom_exceptions import NotFoundError

conn = DbConnection().get_connection()


def save(course: Course):
    conn.execute("INSERT INTO course (name, price, teacher_id) VALUES (?, ?, ?)",
                 (course.name, course.price, course.teacher_id))
    conn.commit()


def get_all() -> list:
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, price, teacher_id FROM course")
    query_result = cursor.fetchall()
    courses = []
    for row in query_result:
        course = Course(int(row[0]), row[1], row[2], row[3])
        courses.append(course)

    return courses


def find_by_teacher_id(teacher_id: int) -> list:
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT id, name, price, teacher_id FROM course WHERE teacher_id = {teacher_id}")
    query_result = cursor.fetchall()
    courses = []
    for row in query_result:
        course = Course(int(row[0]), row[1], row[2], int(row[3]))
        courses.append(course)

    return courses


def find_one_by_id(course_id: int) -> list:
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT id, name, price, teacher_id FROM course WHERE id = {course_id}")
    rows = cursor.fetchall()
    result = rows[0]
    if len(result) == 0:
        raise NotFoundError

    course = Course(int(result[0]), result[1], result[2], int(result[3]))

    return course
