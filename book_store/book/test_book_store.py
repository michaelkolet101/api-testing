import logging
import pytest
import allure
from book_api import Book_store, to_delete, data_1, list_of_books

my_store = Book_store('https://bookstore.toolsqa.com/BookStore/v1/')
LIST_OF_RESULT = [200, 401]


@allure.step
def test_get_books():
    status = my_store.get_books()
    assert status in LIST_OF_RESULT
    assert 'books' in my_store.get_books_data()
    logging.info(f"test_get_books, status = {status}")

@allure.step
def test_post_list_of_books():
    status = my_store.post_list_of_books(list_of_books)
    assert status in LIST_OF_RESULT
    logging.info(f"test_post_list_of_books, status = {status}")

@allure.step
def test_delete_user():
    status = my_store.delete_user('123456')
    assert status in LIST_OF_RESULT
    msg = ""
    if status != 200:
        msg = 'User not authorized!'
    logging.info(f"test_delete_user, status = {status} \n {msg}")


@allure.step
def test_get_book_by_ISBN():
    status = my_store.get_book_by_ISBN("12366")
    assert status in LIST_OF_RESULT
    msg = ""
    if status != 200:
        msg = 'book not found!'
    logging.info(f"test_get_book_by_ISBN, status = {status} \n {msg}")


@allure.step
def test_delete_book_by_data():
    status = my_store.delete_book_by_data(to_delete)
    assert status in LIST_OF_RESULT
    msg = ""
    if status != 200:
        msg = 'book not found!'
    logging.info(f"test_delete_book_by_data, status = {status} \n {msg}")


@allure.step
def test_change_data():
    status = my_store.change_data(data_1, '123456')
    assert status in LIST_OF_RESULT
    msg = ""
    if status != 200:
        msg = 'book not found!'
    logging.info(f"test_change_data, status = {status} \n {msg}")

