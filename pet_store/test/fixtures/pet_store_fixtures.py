
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

@pytest.fixture()
def MPet() -> Pet:
    category = Category(234, g_s())
    photoUrls = ["https://en.wikipedia.org/wiki/Cat#/media/File:Cat_poster_1.jpg"]
    tags = [{"id": 200, "name": "jonson"}]
    my_pet = Pet(random.randint(0, 1000), g_s(), category, photoUrls, tags, "available")
    return my_pet


my_pet = Pet(random.randint(0, 1000),
             g_s(),
             Category(234, g_s()),
             ["https://en.wikipedia.org/wiki/Cat#/media/File:Cat_poster_1.jpg"],
             [{"id": 200, "name": "jonson"}],
             "available")

@pytest.fixture
def my_store(set_url):
    my_store = Store(set_url)
    return my_store


@pytest.fixture
def new_pet_store(set_url):
    my_store = PetApi(set_url)
    return my_store

@pytest.fixture
def MOrder() -> Order:
    my_order = Order(3242, 3424, 1, datetime.datetime.now(), "placed", False)
    return my_order

@pytest.fixture()
def MUser() -> User:
    my_user = User(random.randint(0, 10000), g_s(), "2wfs324", "Deb", "Fel", "michaelkolet@gmail.com", random.randint(0, 100000), 5)
    return my_user


@pytest.fixture
def users(set_url) -> User:
    return User(set_url)


def uesrs_list() -> [User]:
    U1 = User(random.randint(0, 10000), g_s(), "2wfs324", "tal", "tal", "tal@gmail.com", 234152433, 5)
    U2 = User(random.randint(0, 10000), g_s(), "2wfs324", "dan", "dan", "dan@gmail.com", 836452872, 5)
    list_of_users = [U1, U2]
    return list_of_users
