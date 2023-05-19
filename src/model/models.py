# User Class
class User:
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

    def __str__(self) -> str:
        return f"ID: {self.id}, Nombre: {self.name}, Correo: {self.email}"

# Teacher Class
class Teacher(User):
    def __init__(self, id: int, name: str, email: str, speciality: str):
        super().__init__(id, name, email)
        self.speciality = speciality

# Student Class
class Student(User):
    def __init__(self, id, name, email):
        super().__init__(id, name, email)
        self.balance = 0

# Course Class
class Course:
    def __init__(self, id,  name, price):
        self.id = id
        self.name = name
        self.price = price

# Bill Class


class Bill:
    def __init__(self, id, user_id, course_id):
        self.id = id
        self.user_id = user_id
        self.course_id = course_id
