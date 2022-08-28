from models.BaseObj import BaseObj


class ReplaceIsbn(BaseObj):
    def __init__(self, user_id: str, isbn: str):

        self._userId = user_id
        self._isbn = isbn

    @property
    def isbn(self):
        """Gets the isbn of this Model.  # noqa: E501
        :return: The isbn of this Model.  # noqa: E501
        :rtype: str
        """
        return self._isbn


