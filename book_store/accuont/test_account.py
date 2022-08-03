import logging

from Account import acuont, ac_1, ac_2, ac_3
from Account import Account
import pytest
import allure


LIST_OF_RESILT = [200, 201, 204, 400, 401, 404, 406]

@allure.step
def test_Authorized():
    status = acuont.Authorized(ac_1)
    assert status in LIST_OF_RESILT
    logging.info(f"test_Authorized status: {status}")

@allure.step
def test_Generate_token():
    ans = acuont.Generate_token(ac_1)
    assert ans['status'] == 'Success'
    logging.info(f"test_Generate_token, \ndict is: {ans}")

@allure.step
def test_add_user_account():
    status = acuont.add_user_account(ac_3)
    assert status in LIST_OF_RESILT
    msg = ""
    if status == 406:
        msg = "msg is: There is already a user"
    logging.info(f"test_add_user_account, status = {status}\n {msg}!!!")

@allure.step
def test_delete_user_by_id():
    # it is user id ask swagger
    status = acuont.delete_user_by_id('88fc69d2-db32-4846-bd1f-d2df2eacf10a')
    assert status in LIST_OF_RESILT
    msg = ""
    if status == 401:
        msg = 'msg is: user not authoriz!!!'
    logging.info(f'test_delete_user_by_id, status is: {status}\n {msg}')

@allure.step
def test_get_user_by_id():
    status = acuont.get_user_by_id('88fc69d2-db32-4846-bd1f-d2df2eacf10a')
    assert status in LIST_OF_RESILT
    if status == 401:
        msg = 'msg is: user not found!!!'
    logging.info(f'get_user_by_id, status is: {status}\n {msg}')




