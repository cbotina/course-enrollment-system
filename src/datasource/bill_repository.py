from model.models import Bill
from config.database import DbConnection

conn = DbConnection().get_connection()


def save(bill: Bill):
    conn.execute("INSERT INTO bill (user_id, course_id, ) VALUES (?, ?)",
                 (bill.user_id, bill.course_id))
    conn.commit()
