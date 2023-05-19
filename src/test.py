from utils.initializers import create_tables
from model.models import Teacher
from datasource.teacher_repository import save, find_all

teacher = Teacher(0, 'carlos', 'carlos@gmail.com', 'ingeniero')

save(teacher)

print([str(x) for x in find_all()])

