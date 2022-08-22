import logging
import pytest
import allure
from store import Store, my_store, order_1
import json



@allure.step
def test_add_new_order():
    assert 200 == my_store.delete_order_by_id(order_1['id'])
    status = my_store.add_new_order(order_1)
    logging.info(status)
    logging.info(order_1['id'])
    assert 200 == status
    data = my_store.find_order_by_id(order_1['id'])
    d = json.loads(data)
    logging.info(d)
    assert order_1['id'] in d.values()


@allure.step
def test_find_order_by_id():
    order_id = order_1['id']
    logging.info(order_id)
    assert 200 == my_store.delete_order_by_id(order_id)
    assert 200 == my_store.add_new_order(order_1)
    data = my_store.find_order_by_id(order_id)
    d = json.loads(data)
    logging.info(d)
    assert d['id'] == order_1['id']



@allure.step
def test_delete_order_by_id():
    assert 200 == my_store.add_new_order(order_1)
    order_id = order_1['id']
    logging.info(order_id)
    assert 200 == my_store.delete_order_by_id(order_id)
    data = my_store.find_order_by_id(order_id)
    logging.info(data)
    assert data == 'Order not found'



@allure.step
def test_get_inventory():
    data = my_store.get_inventory()
    logging.info(f"test_get_inventory, data = {data}")
    assert 'approved' in data



