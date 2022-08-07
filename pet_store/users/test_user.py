import json
import logging
import pytest
import allure
from user import users, user_1, user_2, user_3, user_4, list_of_users

@allure.step
def test_create_user():
    user_name = user_1["username"]
    logging.info(user_name)
    status = users.create_user(user_1)
    logging.info(status)
    assert 200 == status
    data = users.get_user_by_user_name(user_name)
    logging.info(data)
    assert data['username'] == user_name

@allure.step
def test_create_with_list():
    my_list = list_of_users
    logging.info(list_of_users)
    j_list = [json.dumps(item) for item in list_of_users]
    status = users.create_with_list(json.dumps(list_of_users))
    logging.info(status)
    assert (status == 200)


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
    assert users.create_user(user_1) == 200
    name = user_1['username']
    logging.info(name)
    assert name == users.get_user_by_user_name(name)['username']


@allure.step
def test_Update_user():
    assert 200 == users.create_user(user_3)
    user_6 = user_3
    logging.info(user_6)
    user_6['username'] = 'max'
    logging.info(user_6)
    assert 200 == users.Update_user(user_6, user_3['username'])


@allure.step
def test_delete_username():
    assert 200 == users.create_user(user_4)
    status = users.delete_username(user_4['username'])
    logging.info(status.status_code)
    assert 200 == status.status_code

