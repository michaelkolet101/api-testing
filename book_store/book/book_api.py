import json
import requests
from book_store.accuont.Account import acuont, ac_1


class Book_store():

    def __init__(self, url: str):
        self._url = url
        self._headrs = {'accept': 'application/json',
                        'authorization': 'Basic b21lcm1hem9yMTI6T21lcjEyMyE==true'
                        }
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

    def post_list_of_books(self, book_list: json):
        """
        :param book_list:
        :return: status
        """
        response = self._session.post(f'{self._url}/Books', data=book_list)
        return response

    def delete_user(self, user_id: str):
        """
        :param user_id:
        :return: status
        """
        response = self._session.delete(f'{self._url}/Books?UserId={user_id}')
        return response

    def get_book_by_ISBN(self, ISBN_book: str):
        """
        :param ISBN_book:
        :return: json
        """
        response = self._session.get(f'{self._url}/Books?U?ISBN={ISBN_book}')
        return response.json()

    def delete_book_by_data(self, data: json):
        """
        :param data: {userID:??? ,ISBN_book:???}
        :return: status
        """
        response = self._session.delete(f'{self._url}/Books', data=data)
        return response.status_code()

    def change_data(self, new_data: json, ISBN_book: str):
        """
        :param new_data:
        :param ISBN_book:
        :return: status
        """
        response = self._session.post(f'{self._url}/Books/{ISBN_book}', data=new_data)
        return response.status_code


to_delete = {
    "isbn": "1234567",
    "userId": "1234567"
}

data_1 = {
    "isbn": "1234567",
    "userId": "1234567"
}
u_id = ""
list_of_books = {
        "userId": u_id,
        "collectionOfIsbns": [
            {
                "isbn": "1212"
            },
            {
                "isbn": "1313"
            }
        ]
    }
def main():

    my_store = Book_store('https://bookstore.toolsqa.com/BookStore/v1/')

    print(my_store.get_books())
    print(my_store.get_books_data())

    data = acuont.add_user_account_get_id(ac_1)
    acuont.Generate_token(ac_1)
    print(acuont.Authorized(ac_1))
    print(data)
    u_id = data['userID']
    print(u_id)
    list_of_books['userID'] = u_id
    acuont.Generate_token(ac_1)
    print(my_store.post_list_of_books(list_of_books))
    print('delete_user', my_store.delete_user(u_id))
    # print(my_store.get_book_by_ISBN("12366"))
    # print('delete_book_by_data', my_store.delete_book_by_data(to_delete))
    # print('change_data', my_store.change_data(data_1, '123456'))


if __name__ == "__main__":
    main()