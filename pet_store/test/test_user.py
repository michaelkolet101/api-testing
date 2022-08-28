import json
import logging
import pytest

from pet_store.test.fixtures.pet_store_fixtures import *




def verification_user_add(users ,MUser):
    user_name = MUser.username
    logging.info(user_name)
    status = users.create_user(MUser)
    logging.info(status)
    assert 200 == status
    data = users.get_user_by_user_name(user_name)
    logging.info(data)
    assert data.username == user_name


def test_create_user(MUser, users):
    verification_user_add(users ,MUser)

def test_create_with_list(uesrs_list, users):

    user_name1 = uesrs_list()[0].username
    user_name2 = uesrs_list()[1].username
    logging.info(uesrs_list)
    j_list = [json.dumps(item) for item in uesrs_list]
    status = users.create_with_list(json.dumps(uesrs_list))
    logging.info(status)
    assert status == 200
    assert user_name1 == users.get_user_by_user_name(user_name1).username
    assert user_name2 == users.get_user_by_user_name(user_name2).username



def test_login(MUser, users):
    verification_user_add(users ,MUser)
    assert 200 == users.login(MUser.username, MUser.password)
    logging.info("test to login")



def test_logout(MUser, users):
    verification_user_add(users ,MUser)
    users.login(MUser.username, MUser.password)
    assert 200 == users.logout()
    logging.info("test_logout")



def test_get_user_by_user_name(MUser, users):
    verification_user_add(users ,MUser)
    name = MUser.username
    logging.info(name)
    assert name == users.get_user_by_user_name(name).username


def test_Update_user(MUser, users):
    verification_user_add(users ,MUser)
    MUser.username = "michael!!!"
    res_put = users.Update_user(MUser)
    assert res_put.json()["username"] == MUser.username


def test_delete_username(MUser, users):
    verification_user_add(users ,MUser)
    status = users.delete_username(User.username)
    logging.info(status.status_code)
    assert 200 == status.status_code
    assert 404 == users.get_user_by_user_name
