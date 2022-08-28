
from fixtures import *

logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.ERROR)
mylogger = logging.getLogger()



def test_post_user(My_Details, My_User):
    global user_ID, token
    mylogger.info("test for create new user")
    res_post_user = accountApi.post_user(My_Details)
    assert res_post_user.status_code == 201
    assert res_post_user.json()["username"] == My_Details.userName
    global user_ID, token
    user_ID = res_post_user.json()["userID"]
    res_post_token = accountApi.post_generate_token(My_User)
    token = res_post_token.json()["token"]
    assert accountApiToken.get_user_by_id(user_ID).id == user_ID

def test_post_authorized(My_User):
    mylogger.info("test for user authorization")
    res_post = accountApiToken.post_authorized(My_User)
    assert res_post.status_code == 200
    assert res_post.json() is True


def test_post_generate_token(My_User):
    mylogger.info("test for generate new token")
    res_post = accountApi.post_generate_token(My_User)
    assert res_post.status_code == 200
    global token
    token = res_post.json()["token"]
    assert len(token) > 5


def test_get_user_by_id():
    mylogger.info("test for get user by id")
    res_get = accountApiToken.get_user_by_id(user_ID)
    assert res_get.id == user_ID
    mylogger.info(res_get.id)


def test_delete_user_by_id():
    mylogger.info("test for delete user by id")
    res_delete = accountApiToken.delete_user_by_id(user_ID)
    assert res_delete.status_code == 204
    res_get = accountApiToken.get_user_by_id(user_ID)
    assert res_get.status_code == 401


def test_get_all_store_books():
    mylogger.info("test for get all books in the store")
    res_get = bookStoreApi.get_all_store_books()
    assert res_get.status_code == 200
    mylogger.info(res_get.json())


def test_post_books(My_List_Of_Books):
    mylogger.info("test for create list of books")
    res_delete = bookStoreApiToken.delete_books_by_userid(user_ID)
    assert res_delete.status_code == 204
    res_post = bookStoreApiToken.post_books(My_List_Of_Books[0])
    assert res_post.status_code == 201
    mylogger.info(f"Success! {res_post.json()}")
    assert My_List_Of_Books[0] in bookStoreApi.get_all_store_books()['books'].value


def test_delete_books_by_userid():
    res_delete = bookStoreApiToken.delete_books_by_userid(user_ID)
    assert res_delete.status_code == 204
    mylogger.info(res_delete.text)


def test_get_by_isbn():
    mylogger.info("test for get books by isbn")
    res_get = bookStoreApi.get_all_store_books()
    assert res_get.status_code == 200
    assert res_get.json()["books"][0]["isbn"]
    res_get2 = bookStoreApi.get_by_isbn(res_get.json()["books"][0]["isbn"])
    assert res_get2.status_code == 200
    assert res_get2.json()["isbn"] == res_get.json()["books"][0]["isbn"]


def test_delete_books_by_string_object(My_List_Of_Books,My_String_Object):
    mylogger.info("test for delete books by string object (isbn, userid)")
    res_get = accountApiToken.get_user_by_id(user_ID)
    assert res_get.status_code == 200
    res_post = bookStoreApiToken.post_books(My_List_Of_Books)
    assert res_post.status_code == 201
    res_delete = bookStoreApiToken.delete_books_by_string_object(My_String_Object)
    res_get2 = accountApiToken.get_user_by_id(user_ID)
    assert res_delete.status_code == 204
    mylogger.info("book deleted successfully!")
    books_before = res_get.json()["books"]
    books_after = res_get2.json()["books"]
    assert len(books_after) < len(books_before)


def test_put_isbn(My_List_Of_Books,My_String_Object,My_Replace_Isbn):
    mylogger.info("test for change isbn of user's book list")
    res_post = bookStoreApiToken.post_books(My_List_Of_Books)
    assert res_post.status_code == 201
    res_get = accountApiToken.get_user_by_id(user_ID)
    assert res_get.status_code == 200
    books = res_get.json()["books"]
    res_put = bookStoreApi.put_isbn(books[0]["isbn"], My_Replace_Isbn)
    assert res_put.status_code == 200
    assert res_put.json()["books"][0]["isbn"] == My_Replace_Isbn.isbn

