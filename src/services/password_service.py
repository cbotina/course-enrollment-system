import hashlib


def hash_password(input_password: str):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(input_password.encode())
    hashed_input_password = hash_algorithm.hexdigest()
    return hashed_input_password


def check_password(input_password: str, hashed_db_password: str):
    return (hash_password(input_password) == hashed_db_password)
