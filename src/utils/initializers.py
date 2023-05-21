import sqlite3
from config.database import DbConnection


def create_tables():
    conn = DbConnection().get_connection()
    # Create students table
    conn.execute('''CREATE TABLE IF NOT EXISTS student
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    password TEXT NOT NULL,
                    balance REAL DEFAULT 0);''')

    # Create teacher table
    conn.execute('''CREATE TABLE IF NOT EXISTS teacher
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    password TEXT NOT NULL,
                    speciality TEXT NOT NULL);''')

    # Create course table
    conn.execute('''CREATE TABLE IF NOT EXISTS course
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    price REAL NOT NULL,
                    teacher_id INT NOT NULL,
                    FOREIGN KEY(teacher_id) REFERENCES teacher(id));''')

    # Create bill table
    conn.execute('''CREATE TABLE IF NOT EXISTS bill
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_id INT NOT NULL,
                    course_id INT NOT NULL,
                    FOREIGN KEY (student_id) REFERENCES student(id),
                    FOREIGN KEY (course_id) REFERENCES course(id));''')
