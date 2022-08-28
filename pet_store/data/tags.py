# coding: utf-8
from pet_store.data.baseObj import baseObj


class Tags(baseObj):

    def __init__(self, id: int, name: str):
        self._id = id
        self._name = name

    @property
    def id(self):
        """Gets the id of this Tags.
        :return: The id of this Tags.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Tags.
        :param id: The id of this Tags.
        :type: int
        """
        self._id = Id

    @property
    def name(self):
        """Gets the name of this Tags.
        :return: The name of this Tags.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Tags.
        :param name: The name of this Tags.  # noqa: E501
        :type: str
        """
        self._name = name
