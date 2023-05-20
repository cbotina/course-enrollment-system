from model.models import User


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


class SessionData(metaclass=SingletonMeta):
    user = None

    def get_user(self):
        return self.user

    def set_user(self, user: User):
        self.user = user
