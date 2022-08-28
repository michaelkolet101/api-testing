from models.BaseObj import BaseObj


class LoginViewModel(BaseObj):
    def __init__(self, user_name: str, password: str):

        self._user_name = user_name
        self._password = password


