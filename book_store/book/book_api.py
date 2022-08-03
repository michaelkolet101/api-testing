import json
import requests


class Book_store:
    def __init__(self, url: str):
        self._url = url
        self._headrs = {'accept': 'application/json'}
        self._session = requests.session()
        self._session.headers = self._headrs

    def get_books(self):
        """
        :return: list of all books
        """
        response = self._session.get(f'{self._url}/Books')
        return response.status_code

    def get_books_data(self):
        """
        :return: list of all books
        """
        response = self._session.get(f'{self._url}/Books')
        return response.json()

    def post_list_of_books(self, book_list: dict):
        """
        :param book_list:
        :return: status
        """
        response = self._session.post(f'{self._url}/Books', data=book_list)
        return response.status_code

    def delete_user(self, user_id: str):
        """
        :param user_id:
        :return: status
        """
        response = self._session.delete(f'{self._url}/Books?UserId={user_id}')
        return response.status_code

    def get_book_by_ISBN(self, ISBN_book: str):
        """
        :param ISBN_book:
        :return: json
        """
        response = self._session.get(f'{self._url}/Books?U?ISBN={ISBN_book}')
        return response.status_code

    def delete_book_by_data(self, data: json):
        """
        :param data: {userID:??? ,ISBN_book:???}
        :return: status
        """
        response = self._session.delete(f'{self._url}/Books', data=data)
        return response.status_code

    def change_data(self, new_data: json, ISBN_book: str):
        """
        :param new_data:
        :param ISBN_book:
        :return: status
        """
        response = self._session.post(f'{self._url}/Books/{ISBN_book}', data=new_data)
        return response.status_code


list_of_books = {"userId": "1234", "collectionOfIsbns": [
    {
        "isbn": "1212"
    },
    {
        "isbn": "1313"
    }
]
                 }

to_delete = {
    "isbn": "1234567",
    "userId": "1234567"
}

data_1 = {
    "isbn": "1234567",
    "userId": "1234567"
}

my_store = Book_store('https://bookstore.toolsqa.com/BookStore/v1/')

print(my_store.get_books())
print(my_store.get_books_data())
print(my_store.post_list_of_books(list_of_books))
print('delete_user', my_store.delete_user('555'))
print(my_store.get_book_by_ISBN("12366"))
print(my_store.delete_book_by_data(to_delete))
print(my_store.change_data(data_1, '123456'))
