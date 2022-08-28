import pytest
from models.book_model import Book
from models.login_view_model import LoginViewModel
from models.register_view_model import RegisterView
from models.collection_of_isbn import CollectionOfIsbn
from models.add_list_of_books import AddListBooks
from models.user import CreateUserResult
from models.get_user_result import GetUserResult
from models.replace_isbn import ReplaceIsbn
from models.string_object import StringObject
from api.account_api import AccountApi
from api.book_store_api import BookStoreApi
import logging
import datetime
import sys





def get_url():
    url = "https://bookstore.toolsqa.com"
    if len(sys.argv) > 1:
        url = sys.argv[1]
    return url

user_ID = ""
token = ""

accountApi = AccountApi(get_url())
bookStoreApi = BookStoreApi(get_url())
bookStoreApiToken = BookStoreApi(get_url())
accountApiToken = AccountApi(get_url())
logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.ERROR)
mylogger = logging.getLogger()




@pytest.fixture()
def My_Details() -> RegisterView:
    register_view = RegisterView("michael24", "michael24@gamil")
    return register_view


@pytest.fixture()
def My_User() -> LoginViewModel:
    login_view = LoginViewModel("michael24", "michael24@gamil")
    return login_view


@pytest.fixture()
def My_List_Of_Books() -> AddListBooks:
    C = CollectionOfIsbn("12341111")
    addListOfBooks = AddListBooks(user_ID, [C])
    return addListOfBooks


@pytest.fixture()
def My_Book() -> Book:
    book = Book("1234", "flower", "Store Flower",
                "deb fellous", datetime.datetime(2012, 26, 5), "paris", 566, "teva",
                "https://www.flower.com/")
    return book


@pytest.fixture()
def My_String_Object() -> StringObject:
    string_object = StringObject("928492034182304", user_ID)
    return string_object


@pytest.fixture()
def My_Replace_Isbn() -> ReplaceIsbn:

    replace_isbn = ReplaceIsbn(user_ID, "gdghfyjfyggdsdytfj")
    return replace_isbn
