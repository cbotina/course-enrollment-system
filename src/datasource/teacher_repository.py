from model.models import Teacher
from config.database import DbConnection

conn = DbConnection().get_connection()


def save(teacher: Teacher):
    conn.execute("INSERT INTO teacher (name, email, password, speciality) VALUES (?, ?, ?, ?)",
                 (teacher.name, teacher.email, teacher.password, teacher.speciality))
    conn.commit()


def find_all() -> list:
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, name, email, password,  speciality FROM teacher")
    query_result = cursor.fetchall()
    users = []
    for row in query_result:
        user = Teacher(int(row[0]), row[1], row[2], row[3], row[4])
        users.append(user)

    return users
