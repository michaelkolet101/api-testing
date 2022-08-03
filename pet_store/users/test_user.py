import json
import logging
from user import users, user_1, user_2, user_3, user_4 ,list_of_users


def test_create_user():
    logging.info('test_create_user')
    assert 200 == users.create_user(user_1) or 500 == users.create_user(user_1)


def test_create_with_list():
    status = users.create_with_list(json.dumps(list_of_users))
    assert (status == 200 or status == 500)
    logging.info('test to test_create_with_list')


def test_login():
    assert 200 == users.create_user(user_4)
    assert 200 == users.login(user_4["username"], user_4["password"])
    logging.info("test to login")


def test_logout():
    assert 200 == users.create_user(user_3)
    assert 200 == users.logout()


def test_get_user_by_user_name():
    # the user saved in the system
    assert 'theUser' == users.get_user_by_user_name('theUser')['username']
    logging.info('test_get_user_by_user_name')


def test_Update_user():
    assert 200 == users.create_user(user_3)
    user_6 = user_3
    user_6['username'] = 'max'
    assert 200 == users.Update_user(user_6, user_3['username'])
    logging.info('test_Update_user')


def test_delete_username():
    assert 200 == users.create_user(user_4)
    assert 200 == users.delete_username(user_4['username'])
    logging.info("test_delete_username")
