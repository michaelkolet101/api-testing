import pytest
import allure
import sys
from generat_string import g_s
import logging
from pet_api import PetApi
from pet_api import pet_1

# sys.argv[1]
url = 'https://petstore3.swagger.io/api/v3'
pet_store = PetApi(url)


@allure.step
def test_to_get_pet_by_id():
    pet_id = pet_1['id']
    logging.info(pet_id)
    assert 200 == pet_store.delete_pet_by_id(pet_id)
    status = pet_store.add_new_pet(pet_1)
    assert status == 200
    logging.info(f"add pet status = {status}")
    assert 200 == status
    data = pet_store.get_pet_ById(pet_1['id'])
    logging.info(data)
    assert data['id'] == pet_id



@allure.step
def test_add_new_pet():
    pet_id = pet_1['id']
    logging.info(pet_id)
    #assert 200 == pet_store.delete_pet_by_id(pet_id)
    status = pet_store.add_new_pet(pet_1)
    logging.info(status)
    assert status == 200
    status_2 = pet_store.get_pet_ById_status(pet_1['id'])
    logging.info(f'get_pet_ById_status, {status_2}')
    assert status_2 == 200



@allure.step
def test_to_put_update_pet():
    pet_id = pet_1['id']
    assert 200 == pet_store.delete_pet_by_id(pet_id)
    assert 200 == pet_store.add_new_pet(pet_1)
    new_name = g_s()
    logging.info(new_name)
    pet_1['name'] = new_name
    status = pet_store.update_pet_by_id(pet_1['id'], pet_1)
    logging.info(status)
    data = pet_store.get_pet_ById(pet_1['id'])
    logging.info(data)
    assert pet_1['name'] == new_name


@allure.step
def test_find_by_status():
    lst = pet_store.find_by_status("available")
    logging.info(lst)
    check = True
    for itm in lst:
        if itm['status'] != "available":
            check = False
    logging.info(f"test to test_find_by_status, check: {check}")
    assert check


# TODO its dont work need to fix that
@allure.step
def test_find_by_tags():
    pet_id = pet_1['id']
    logging.info(pet_id)
    assert 200 == pet_store.delete_pet_by_id(pet_id)
    assert 200 == pet_store.add_new_pet(pet_1)
    logging.info(pet_1['tags'])
    data = pet_store.find_by_tags(pet_1['tags'])
    logging.info(data)


@allure.step
def test_update_pet_by_id_post():
    pet_id = pet_1['id']
    logging.info(pet_id)
    assert 200 == pet_store.delete_pet_by_id(pet_id)
    assert 200 == pet_store.add_new_pet(pet_1)
    assert 200 == pet_store.update_pet_by_id_post(pet_1['id'], 'shaltiel', "sold")
    data = pet_store.get_pet_ById(pet_1['id'])
    logging.info(f'test_update_pet_by_id_post, data = {data}')
    assert data['name'] == 'shaltiel'
    assert data['status'] == 'sold'

@allure.step
def test_delete_pet_by_id():
    pet_id = pet_1['id']
    assert 200 == pet_store.add_new_pet(pet_1)
    data = pet_store.get_pet_ById(pet_1['id'])
    logging.info(f"befor delet - {data}")
    logging.info(pet_id)
    status = pet_store.delete_pet_by_id(pet_id)
    logging.info(f"delete_pet_by_id, status: {status}")
    assert status == 200
    data = pet_store.get_pet_ById(pet_1['id'])
    logging.info(data)
    assert 'pet not pound' == data

@allure.step
def test_upload_image_by_id():
    assert 200 == pet_store.delete_pet_by_id(pet_1['id'])
    assert 200 == pet_store.add_new_pet(pet_1)
    d = pet_store.get_pet_ById(pet_1['id'])
    logging.info(d)
    assert len(d['photoUrls']) == 1
    status = pet_store.upload_image_by_id(pet_1['id'], 'my_dog.jpg')
    logging.info(f'upload_image_by_id ,status: {status}')
    assert 200 == status
    d = pet_store.get_pet_ById(pet_1['id'])
    logging.info(d)
    assert len(d['photoUrls']) == 2
    logging.info(f"test_upload_image_by_id, status = {status}")