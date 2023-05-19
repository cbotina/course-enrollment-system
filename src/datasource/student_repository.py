from model.models import Student
from config.database import DbConnection

conn = DbConnection().get_connection()


def save(student: Student):
    conn.execute("INSERT INTO student (name, email) VALUES (?, ?)",
                 (student.name, student.email))
    conn.commit()


def find_all() -> list:
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email FROM student")
    query_result = cursor.fetchall()
    users = []
    for row in query_result:
        user = Student(int(row[0]), row[1], row[2])
        users.append(user)

    return users