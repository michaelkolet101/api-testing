from pet_store.data.pet import *
from pet_store.api.pet_api import *
from pet_store.data.order import *
import pytest
from pet_store.data.generat_string import g_s
import random
url = 'https://petstore3.swagger.io/api/v3'

@pytest.fixture()
def MPet() -> Pet:
    category = Category(234, g_s())
    photoUrls = ["https://en.wikipedia.org/wiki/Cat#/media/File:Cat_poster_1.jpg"]
    tags = [{"id": 200, "name": "jonson"}] #[Tags(3453445, "tag1")]
    my_pet = Pet(random.randint(0, 1000), g_s(), category, photoUrls, tags, "available")
    return my_pet

@pytest.fixture
def new_pet_store():
    my_store = PetApi(url)

@pytest.fixture
def MOrder() -> Order:
    my_order = Order(3242, 3424, 1, datetime.datetime.now(), "placed", False)
    return my_order

