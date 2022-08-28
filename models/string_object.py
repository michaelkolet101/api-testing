from models.BaseObj import BaseObj


class StringObject(BaseObj):
    def __init__(self, isbn: str, user_id: str):

        self._isbn = isbn
        self._userId = user_id


