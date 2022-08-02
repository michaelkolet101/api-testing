import pytest
import logging
from user import User
from user import users, user_1, user_2


def test_create_user():
    logging.info('test_create_user')
    assert 200 == users.create_user(user_1) or 500 == users.create_user(user_1)


