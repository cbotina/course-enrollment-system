# User Class
class User:
    def __init__(self, id: int, name: str, email: str, password: str):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def __str__(self) -> str:
        return f"ID: {self.id}, Nombre: {self.name}, Correo: {self.email}"

# Teacher Class


class Teacher(User):
    def __init__(self, id: int, name: str, email: str, password: str, speciality: str):
        super().__init__(id, name, email, password)
        self.speciality = speciality

# Student Class


class Student(User):
    def __init__(self, id: int, name: str, email: str, password: str):
        super().__init__(id, name, email, password)
        self.balance = 0

# Course Class


class Course:
    def __init__(self, id,  name, teacher_id, price):
        self.id = id
        self.name = name
        self.teacher_id = teacher_id
        self.price = price

    def __str__(self) -> str:
        return f'{self.id}. {self.name}'

# Bill Class


class Bill:
    def __init__(self, id, student_id, course_id):
        self.id = id
        self.student_id = student_id
        self.course_id = course_id
