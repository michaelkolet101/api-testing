from models.BaseObj import BaseObj
import re


class RegisterView(BaseObj):
    def __init__(self, userName: str, password: str):

        self._userName = userName
        self._password = password

    @property
    def userName(self):
        """Gets the userName of this Model.  # noqa: E501
        :return: The userName of this Model.  # noqa: E501
        :rtype: str
        """
        return self._userName

    @userName.setter
    def userName(self, userName):
        """Sets the userName of this Model.
        :param userName: The username of this Model.  # noqa: E501
        :type: str
        """
        self._userName = userName

    @property
    def password(self):
        """Gets the password of this Model.  # noqa: E501
        :return: The password of this Model.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this model.
        :param password: The password of this Model.  # noqa: E501
        :type: str
        """

        self._password = password
