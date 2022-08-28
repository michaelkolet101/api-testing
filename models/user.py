from models.BaseObj import BaseObj


class User(BaseObj):
    def __init__(self, userId=None, username=None, books=None):

        self._userId = userId
        self._username = username
        self._books = books




