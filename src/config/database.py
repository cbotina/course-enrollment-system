import sqlite3

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    
class DbConnection(metaclass=SingletonMeta):
    conn = sqlite3.connect('data.db')
    
    def get_connection(self):
        return self.conn
        

