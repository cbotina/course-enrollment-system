from utils.initializers import create_tables
from model.models import Teacher
from datasource.teacher_repository import save, find_all

from services.password_service import hash_password, check_password

# import hashlib

# hash_algorithm = hashlib.sha256()

# password = b'hello'

# hash_algorithm.update(password)

# hash_value = hash_algorithm.hexdigest()

# print(hash_value)

# hashed = '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'

# userpassword = 'hello'

# hash_algorithm = hashlib.sha256()

# hash_algorithm.update(userpassword.encode())

# hashed_input_password = hash_algorithm.hexdigest()

# print(hashed_input_password)

# if hashed_input_password == hashed:
#     print("Password is correct!")
# else:
#     print("Password is incorrect!")

passwordinput = 'helloworld'

hashedpassword = hash_password(passwordinput)

print(check_password('helloworld', hashedpassword))
