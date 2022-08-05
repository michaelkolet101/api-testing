import json
import logging
import pytest
import allure
from user import users, user_1, user_2, user_3, user_4 ,list_of_users

@allure.step
def test_create_user():
    user_name = user_1["username"]
    status = users.create_user(user_1)
    logging.info(f'test_create_user. satus = {status}')
    assert 200 == status
    data = users.get_user_by_user_name(user_name)
    assert data['user_name'] == user_name

@allure.step
def test_create_with_list():
    status = users.create_with_list(json.dumps(list_of_users))
    assert (status == 200 or status == 500)
    logging.info('test to test_create_with_list')

@allure.step
def test_login():
    assert 200 == users.create_user(user_4)
    assert 200 == users.login(user_4["username"], user_4["password"])
    logging.info("test to login")

@allure.step
def test_logout():
    assert 200 == users.create_user(user_3)
    assert 200 == users.logout()
    logging.info("test_logout")

@allure.step
def test_get_user_by_user_name():
    # the user saved in the system
    assert 'theUser' == users.get_user_by_user_name('theUser')['username']
    logging.info('test_get_user_by_user_name')

@allure.step
def test_Update_user():
    assert 200 == users.create_user(user_3)
    user_6 = user_3
    user_6['username'] = 'max'
    assert 200 == users.Update_user(user_6, user_3['username'])
    logging.info('test_Update_user')

@allure.step
def test_delete_username():
    assert 200 == users.create_user(user_4)
    assert 200 == users.delete_username(user_4['username'])
    logging.info("test_delete_username")
