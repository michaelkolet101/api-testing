from models.BaseObj import BaseObj
from models.collection_of_isbn import CollectionOfIsbn


class AddListBooks(BaseObj):
    def __init__(self, userId: str, collectionOfIsbns: list):
        self._collectionOfIsbns = collectionOfIsbns
        self._userId = userId
        self._collectionOfIsbns = collectionOfIsbns


