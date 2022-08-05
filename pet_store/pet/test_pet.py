import pytest
import allure
import sys
import logging
from pet_api import PetApi
from pet_api import pet_2, pet_3, pet_4

# sys.argv[1]
url = 'https://petstore3.swagger.io/api/v3'
pet_store = PetApi(url)


@allure.step
def test_to_get_pet_by_id():
    pet_id = pet_2['id']
    assert 200 == pet_store.delete_pet_by_id(pet_id)
    assert 200 == pet_store.add_new_pet(pet_2)
    status = pet_store.get_pet_ById_status()
    assert 200 == status
    data = pet_store.get_pet_ById(pet_2)
    assert data['id'] == pet_id
    logging.info(f"test_to_get_pet_by_id, status is: {status}")


@allure.step
def test_ta_add_new_pet():
    pet_id = pet_2['id']
    assert 200 == pet_store.delete_pet_by_id(pet_id)
    status = pet_store.add_new_pet(pet_2)
    assert 200 == status
    assert 200 == pet_store.get_pet_ById_status(pet_id)
    logging.info(f"test_ta_add_new_pet, status = {status}")

@allure.step
def test_to_put_update_pet():
    pet_id = pet_3['id']
    assert 200 == pet_store.delete_pet_by_id(pet_3['id'])
    assert 200 == pet_store.add_new_pet(pet_3)
    pet_3['name'] = 'moti'
    status = pet_store.update_pet_by_id(pet_3['id'], pet_3)
    data = pet_store.get_pet_ById(pet_id)
    assert pet_3['name'] == data['name']
    logging.info(f"test_to_put_update_pet, status is: {status}")

@allure.step
def test_find_by_status():
    lst = pet_store.find_by_status("available")
    check = True
    for itm in lst:
        if itm['status'] != "available":
            check = False
    logging.info(f"test to test_find_by_status, check: {check}")
    assert check


# TODO its dont work
@allure.step
def test_find_by_tags():
    assert pet_store.delete_pet_by_id(pet_4[id])
    assert 200 == pet_store.add_new_pet(pet_4)
    assert 200 == pet_store.find_by_tags(pet_4['tags'])

@allure.step
def test_update_pet_by_id_post():
    assert 200 == pet_store.add_new_pet(pet_4)
    assert 200 == pet_store.update_pet_by_id_post(pet_4['id'], 'shaltiel', "sold")
    data = pet_store.get_pet_ById(pet_4['id'])
    logging.info('test_updat_pet_by_id_post')
    assert data['name'] == 'shaltiel'
    assert data['status'] == 'sold'

@allure.step
def test_delete_pet_by_id():
    assert 200 == pet_store.add_new_pet(pet_2)
    status = pet_store.delete_pet_by_id(pet_2['id'])
    assert 200 == status
    logging.info(f'test_delete_pet_by_id, status = {status}')
    assert 'pet not pound' == pet_store.get_pet_ById(pet_2['id'])

@allure.step
def test_upload_image_by_id():
    assert 200 == pet_store.delete_pet_by_id(pet_2['id'])
    assert 200 == pet_store.add_new_pet(pet_2)
    d = pet_store.get_pet_ById(pet_2['id'])
    assert len(d['photoUrls']) == 1
    status = pet_store.upload_image_by_id(pet_2['id'], 'my_dog.jpg')
    assert 200 == status
    d = pet_store.get_pet_ById(pet_2['id'])
    assert len(d['photoUrls']) == 2
    logging.info(f"test_upload_image_by_id, status = {status}")