import sqlite3


def create_tables():

    conn = sqlite3.connect('data.db')

    # Create students table
    conn.execute('''CREATE TABLE IF NOT EXISTS student
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    balance REAL DEFAULT 0);''')

    # Create teacher table
    conn.execute('''CREATE TABLE IF NOT EXISTS teacher
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
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
                    user_id INT NOT NULL,
                    course_id INT NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES user(id),
                    FOREIGN KEY (course_id) REFERENCES course(id));''')
