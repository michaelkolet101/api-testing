import logging
import pytest
import allure
from pet_store.test.fixtures.pet_store_fixtures import *
from pet_store.data.order import *
import json


def verification_order_not_exist(my_store, order_id):
    assert 200 == my_store.delete_order_by_id(order_id)
    data = my_store.find_order_by_id(order_id)
    logging.info(data)
    assert data == 'Order not found'


def verification_order_add(my_store, MOrder):
    status = my_store.add_new_order(MOrder)
    logging.info(status)
    logging.info(MOrder.id)
    assert 200 == status
    data = my_store.find_order_by_id(MOrder.id)
    d = json.loads(data)
    logging.info(d)
    assert MOrder.id in d.values()

def test_add_new_order(my_store, MOrder):
    order_id = MOrder.id
    verification_order_not_exist(my_store, order_id)
    verification_order_add(my_store, MOrder)


def test_find_order_by_id(my_store, MOrder):
    order_id = MOrder.id
    logging.info(order_id)
    verification_order_not_exist(my_store, order_id)
    verification_order_add(my_store, MOrder)
    data = my_store.find_order_by_id(order_id)
    d = json.loads(data)
    logging.info(d)
    assert d['id'] == order_1['id']


def test_delete_order_by_id(my_store, MOrder):
    verification_order_add(my_store, MOrder)
    order_id = MOrder.id
    logging.info(order_id)
    verification_order_not_exist(my_store, order_id)


def test_get_inventory(my_store, MOrder):
    data = my_store.get_inventory()
    logging.info(f"test_get_inventory, data = {data}")
    assert 'approved' in data



