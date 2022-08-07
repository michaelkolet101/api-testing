import logging
from generat_string import g_s
from Account import acuont, ac_1
from Account import Account
import pytest
import allure
import sys

# https://bookstore.toolsqa.com/Account/v1
# if sys.argv[1] == None:
#     URL = 'https://bookstore.toolsqa.com/Account/v1/'
# else:
#     URL = sys.argv[1]

URL = "https://bookstore.toolsqa.com/Account/v1"

acuont = Account(URL)


@allure.step
def test_Authorized():
    ac_1['userName'] = g_s()
    data = acuont.add_user_account_get_id(ac_1)
    user_id = data['userID']
    logging.info(f"user_id: {user_id}")
    data_2 = acuont.Generate_token(ac_1)
    authorize = acuont.Authorized(ac_1)
    logging.info(f"authorize: {authorize}, data_of_token is: {data_2}")
    assert authorize == True



@allure.step
def test_Generate_token():
    ac_1['userName'] = g_s()
    assert 400 > acuont.add_user_account(ac_1)
    data = acuont.Generate_token(ac_1)
    assert 'Success' in data.values()
    logging.info(f"test_Generate_token, \ndict is: {data}")


@allure.step
def test_add_user_account():
    ac_1['userName'] = g_s()
    data = acuont.add_user_account_get_id(ac_1)
    logging.info(data)
    user_id = data['userID']
    logging.info(f"user_id: {user_id}")
    assert 'userID' in data.keys()





@allure.step
def test_delete_user_by_id():
    # it is user id ask swagger
    ac_1['userName'] = g_s()
    data = acuont.add_user_account_get_id(ac_1)
    user_id = data['userID']
    logging.info(f"user_id: {user_id}")
    acuont.Generate_token(ac_1)
    authorize = acuont.Authorized(ac_1)
    logging.info(authorize)
    status = acuont.delete_user_by_id(user_id)
    msg = ""
    if status == 401:
        msg = 'msg is: user not authoriz!!!'
    logging.info(f'test_delete_user_by_id, status is: {status}\n {msg}')
    assert status != 401


@allure.step
def test_get_user_by_id():
    ac_1['userName'] = g_s()
    data = acuont.add_user_account_get_id(ac_1)
    logging.info(data)
    user_id = data['userID']
    logging.info(user_id)
    acuont.Generate_token(ac_1)
    auto = acuont.Authorized(ac_1)
    logging.info(auto)
    data = acuont.get_user_by_id(user_id)
    logging.info(data)
    assert 'userId' in data.keys()

