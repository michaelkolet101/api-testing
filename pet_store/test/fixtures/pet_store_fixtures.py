import pytest
from pet_store.api.pet_api import *
from pet_store.api.user import *
from pet_store.api.store import *
from pet_store.data.baseObj import *
from pet_store.data.order import *
from pet_store.data.user import *
from pet_store.data.category import *
from pet_store.data.pet import *
from pet_store.data.tags import *
import sys


import pytest
from pet_store.data.generat_string import g_s
import random


@pytest.fixture()
def set_url():
    url = 'https://petstore3.swagger.io/api/v3'
    if len(sys.argv) > 1:
        url = sys.argv[1]
    return url


pet_1 = {
            "id": random.randint(0, 1000000),
            "name": g_s(),
            "category": {"id": 3, "name": "Dragon"},
            "photoUrls": ["string"],
            "tags": [{"id": 200, "name": "jonson"}],
            "status": "available"
        }


user_1 = {
  "id": random.randint(0, 100000),
  "username": g_s(),
  "firstName": "John",
  "lastName": "James",
  "email": "john@email.com",
  "password": "12345",
  "phone": "12345",
  "userStatus": 1
}


user_2 = {
  "id": random.randint(0, 100000),
  "username": g_s(),
  "firstName": "Mich",
  "lastName": "Kolet",
  "email": "john@email.com",
  "password": "12345",
  "phone": "12345",
  "userStatus": 1
}


order_1 = {
    "id": random.randint(0, 1000),
    "petId": random.randint(0, 1000),
    "quantity": 7,
    "shipDate": "2022-08-01T14:16:51.403Z",
    "status": "approved",
    "complete": True
}


user_3 = {
  "id": random.randint(0, 100000),
  "username": g_s(),
  "firstName": "Mich",
  "lastName": "Kolet",
  "email": "john@email.com",
  "password": "12345",
  "phone": "12345",
  "userStatus": 1
}


user_4 = {
  "id": random.randint(0, 100000),
  "username": g_s(),
  "firstName": "Michl",
  "lastName": "Kolet",
  "email": "john@email.com",
  "password": "12345",
  "phone": "12345",
  "userStatus": 1
}

# def MPet() -> Pet:
#     return Pet(**pet_1)

my_pet = Pet(**pet_1)


@pytest.fixture
def my_store(set_url):
    my_store = Store(set_url)
    return my_store


@pytest.fixture
def new_pet_store(set_url):
    my_pet_store = PetApi(set_url)
    return my_pet_store

@pytest.fixture
def MOrder() -> Order:
    my_order = Order(**order_1)
    return my_order

@pytest.fixture()
def MUser() -> User:
    my_user = User(**user_1)
    return my_user


@pytest.fixture
def users(set_url) -> User:
    return User(set_url)


@pytest.fixture
def uesrs_list() -> [User]:

    list_of_users = [User(**user_1), User(**user_2), User(**user_3), User(**user_4)]
    return list_of_users
