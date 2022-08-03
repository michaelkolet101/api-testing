import logging
import pytest
import allure


from store import Store, my_store, order_1, order_2, order_3
import json

@allure.step
def test_add_new_order():
    assert 200 == my_store.add_new_order(order_1)
    assert isinstance(my_store.find_order_by_id(order_1['id']), dict)
    logging.info("test_add_new_order")

@allure.step
def test_find_order_by_id():
    assert 200 == my_store.add_new_order(order_2)
    data = my_store.find_order_by_id(order_2['id'])
    assert data['id'] == order_2['id']
    logging.info("test_find_order_by_id")


@allure.step
def test_delete_order_by_id():
    assert 200 == my_store.add_new_order(order_1)
    assert 200 == my_store.delete_order_by_id(order_1['id'])
    assert 404 == my_store.find_order_by_id(order_1['id'])
    logging.info("test_delete_order_by_id")


@allure.step
def test_get_inventory():
    status = my_store.get_inventory()
    assert (status == 200 or status == 500)
    logging.info(f"test_get_inventory, status = {status}")


