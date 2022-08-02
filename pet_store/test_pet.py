import pytest
import logging
from pet_api import PetApi
from pet_api import pet_2, pet_3, pet_4

pet_store = PetApi("https://petstore3.swagger.io/api/v3")


def test_to_get_pet_by_id():
    assert 200 == pet_store.add_new_pet(pet_2)
    logging.info("test_to_get_pet_by_id")
    assert 'pet not pound' != pet_store.get_pet_ById(pet_2['id'])
    assert pet_store.get_pet_ById(pet_2['id'])['name'] == pet_2['name']


def test_ta_add_new_pet():
    assert 200 == pet_store.add_new_pet(pet_2)
    logging.info("test_ta_add_new_pet")
    assert 'pet not pound' != pet_store.get_pet_ById(pet_2['id'])


def test_to_put_update_pet():
    assert 200 == pet_store.add_new_pet(pet_3)
    pet_3['name'] = 'moti'
    assert 200 == pet_store.update_pet_by_id(pet_3['id'], pet_3)
    logging.info("test_to_put_update_pet")
    assert pet_3['name'] == pet_store.get_pet_ById(pet_3['id'])['name']


def test_find_by_status():
    lst = pet_store.find_by_status("available")
    check = True
    for itm in lst:
        if itm['status'] != "available":
            check = False
    logging.info("test to test_find_by_status")
    assert check


def test_update_pet_by_id_post():
    assert 200 == pet_store.add_new_pet(pet_4)
    assert 200 == pet_store.update_pet_by_id_post(pet_4['id'], 'shaltiel', "sold")
    data = pet_store.get_pet_ById(pet_4['id'])
    logging.info('test_updat_pet_by_id_post')
    assert data['name'] == 'shaltiel'
    assert data['status'] == 'sold'


def test_delete_pet_by_id():
    assert 200 == pet_store.add_new_pet(pet_2)
    assert 200 == pet_store.delete_pet_by_id(pet_2['id'])
    logging.info('test_delete_pet_by_id')
    assert 'pet not pound' == pet_store.get_pet_ById(pet_2['id'])


def test_upload_image_by_id():
    assert 200 == pet_store.add_new_pet(pet_2)
    d = pet_store.get_pet_ById(pet_2['id'])
    assert len(d['photoUrls']) == 1
    assert 200 == pet_store.upload_image_by_id(pet_2['id'], 'my_dog.jpg')
    d = pet_store.get_pet_ById(pet_2['id'])
    assert len(d['photoUrls']) == 2