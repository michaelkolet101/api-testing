
import logging
import pytest
from pet_store.test.fixtures.pet_store_fixtures import *




def verification_pet_not_exist(new_pet_store,pet_id):
    assert 200 == new_pet_store.delete_pet_by_id(pet_id)
    data = new_pet_store.get_pet_ById_status(pet_id)
    assert data == 404
    logging.info(f"pet {pet_id} delete")


def verification_pet_add(new_pet_store, pet_id):
    status = new_pet_store.add_new_pet(my_pet)
    assert status == 200
    logging.info(f"add pet status = {status}")
    data = new_pet_store.get_pet_ById(pet_id)
    assert data.id == pet_id


def test_to_get_pet_by_id(new_pet_store, MPet):
    pet_id = MPet.id
    logging.info(pet_id)
    verification_pet_not_exist(new_pet_store, pet_id)
    verification_pet_add(new_pet_store, pet_id)

def test_add_new_pet(new_pet_store, MPet):
    pet_id = MPet.id
    logging.info(pet_id)
    verification_pet_not_exist(new_pet_store, pet_id)
    verification_pet_add(new_pet_store, pet_id)

def test_to_put_update_pet(new_pet_store, MPet):
    pet_id = MPet.id
    verification_pet_not_exist(new_pet_store, pet_id)
    verification_pet_add(new_pet_store, pet_id)
    new_name = g_s()
    logging.info(new_name)
    MPet.name = new_name
    status = new_pet_store.update_pet_by_id(MPet.id, MPet)
    logging.info(status)
    data = new_pet_store.get_pet_ById(MPet.id)
    logging.info(data)
    assert MPet.name == new_name



def test_find_by_status(new_pet_store, MPet):
    lst = new_pet_store.find_by_status("available")
    logging.info(lst)
    check = True
    for itm in lst:
        if itm['status'] != "available":
            check = False
    logging.info(f"test to test_find_by_status, check: {check}")
    assert check


def test_find_by_tags(new_pet_store, MPet):
    pet_id = MPet.id
    logging.info(pet_id)
    verification_pet_not_exist(new_pet_store, pet_id)
    verification_pet_add(new_pet_store, pet_id)
    data = new_pet_store.find_by_tags(MPet.tags)
    logging.info(data)


def test_update_pet_by_id_post(new_pet_store, MPet):
    pet_id = MPet.id
    logging.info(pet_id)
    verification_pet_not_exist(new_pet_store, pet_id)
    verification_pet_add(new_pet_store, pet_id)
    assert 200 == new_pet_store.update_pet_by_id_post(MPet.id, 'shaltiel', "sold")
    data = new_pet_store.get_pet_ById(MPet.id)
    assert data.name == 'shaltiel'
    assert data.status == 'sold'


def test_delete_pet_by_id(new_pet_store, MPet):
    pet_id = MPet.id
    verification_pet_add(new_pet_store, pet_id)
    verification_pet_not_exist(new_pet_store, pet_id)


def test_upload_image_by_id(new_pet_store, MPet):
    pet_id = MPet.id
    verification_pet_not_exist(new_pet_store, pet_id)
    verification_pet_add(new_pet_store, pet_id)
    d = new_pet_store.get_pet_ById(pet_id)
    logging.info(d)
    assert len(d['photoUrls']) == 1
    status = new_pet_store.upload_image_by_id(MPet.id, 'my_dog.jpg')
    logging.info(f'upload_image_by_id ,status: {status}')
    assert 200 == status
    d = new_pet_store.get_pet_ById(MPet.id)
    logging.info(d)
    assert len(d['photoUrls']) == 2
    logging.info(f"test_upload_image_by_id, status = {status}")