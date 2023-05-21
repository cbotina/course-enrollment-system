from datasource.bill_repository import save
from utils.initializers import create_tables
from model.models import Teacher, Bill
from datasource.teacher_repository import save, find_all

from services.password_service import hash_password, check_password


from config.database import DbConnection

conn = DbConnection().get_connection()
