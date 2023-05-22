# Course Enrollment System

The Course Enrollment System is a Python-based application that allows users to manage course enrollment, user authentication, and course details. This project is designed to be run in the terminal, providing a command-line interface for easy interaction.

## Getting Started

To run the Course Enrollment System, follow these steps:

1. Clone the project repository to your local machine.
2. Navigate to the root of the project.
3. Run the application by executing the following command:

```bash
python src/main.py
```

## Functionality

The Course Enrollment System provides the following features:

- User Sign Up and Login: Users can create a new account or log in to an existing account to access the system. Passwords are securely hashed using the hashlib library to protect user data.
- User Roles: Users can have the role of a student or a teacher.
- Teacher Functionality:
  - Create Courses: Teachers can create new courses, specifying the associated teacher, course details, and price.
  - View Course Details: Teachers can view details about the courses they have created, including enrolled students.
- Student Functionality:
  - Enroll in Courses: Students can enroll in available courses.
  - View Course Details: Students can view details about the courses they have enrolled in, including the assigned teacher.

## Software Design Patterns

The Course Enrollment System project incorporates the following software design patterns:

### Singleton

The Singleton pattern is used in classes related to session data and database connection. It ensures that only one instance of these classes is created, providing a centralized and efficient way to manage these resources.

### Repository Pattern

The Repository pattern is utilized for interacting with the database (SQLite3). It encapsulates the data access logic and provides a simplified and consistent interface for performing database operations.

## Architecture

The Course Enrollment System follows the Model-View-Controller (MVC) architecture, organizing the codebase into distinct components:

- **Views**: Views represent the menus that users interact with in the terminal. They provide a clear and intuitive interface for users to navigate through the system.
- **Controllers**: Controllers handle user input and execute corresponding actions based on the selected options. They act as intermediaries between the views and the services.
- **Model**: The model represents database tables as objects. It provides an abstraction layer for working with data and ensures separation of concerns between the data and the application logic.
- **Services**: The business logic of the program is located in the 'services' folder. It contains all the methods and functionality required to perform various operations within the Course Enrollment System.

## Conclusion

The Course Enrollment System allows managing course enrollment, user authentication, and course details. Its command-line interface, secure password hashing, and well-defined architecture make it a flexible and scalable software for practicing design patterns, SOLID principles and good practices.

Feel free to explore the project and contribute to its development!
