from models.BaseObj import BaseObj


class CollectionOfIsbn(BaseObj):
    def __init__(self, isbn: str):
        self._isbn = None
        self._isbn = isbn


