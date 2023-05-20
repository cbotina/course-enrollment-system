from model.models import Student
from config.database import DbConnection

conn = DbConnection().get_connection()


def save(student: Student):
    conn.execute("INSERT INTO student (name, email, password) VALUES (?, ?, ?)",
                 (student.name, student.email, student.password))
    conn.commit()


def find_all() -> list:
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email, password FROM student")
    query_result = cursor.fetchall()
    users = []
    for row in query_result:
        user = Student(int(row[0]), row[1], row[2], row[3])
        users.append(user)

    return users


def update_student(student: Student):
    conn.execute("UPDATE student SET name = ?, email = ?, password = ?, balance = ? WHERE id = ?",
                 (student.name, student.email, student.password, student.balance, student.id))
    conn.commit()
