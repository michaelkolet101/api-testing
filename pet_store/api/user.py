import json
import sys
import random
from pet_store.data.user import *
from pet_store.data.generat_string import g_s
import requests


url = "https://petstore3.swagger.io/api/v3/"
if len(sys.argv) > 1:
    url = sys.argv[1]



class Users:

    def __init__(self, url: str):
        self._url = url
        self._headrs = {'accept': 'application/json'}
        self._session = requests.session()
        self._session.headers = self._headrs

    def create_user(self, user_info: User):
        """
        :param user_info:
        :return: status_code
        """
        user_data = user_info.to_json()
        print(user_data)
        res = self._session.post("{https://petstore3.swagger.io/api/v3/user/}", data=user_data)
        return res.json()

    # def create_with_list(self, users_list: json):
    #     """
    #     :param users_list:
    #     :return: status_code
    #     """
    #     response = self._session.post(f'{self._url}/user/createWithList', data=users_list)
    #     return response.status_code
    #
    # def login(self, usr_name: str, password: str):
    #     """
    #     :param usr_name:
    #     :param password:
    #     :return: status_code
    #     """
    #     response = self._session.get(f'{self._url}/user/login?username={usr_name}&password={password}')
    #     return response.status_code
    #
    # def logout(self):
    #     """
    #     logout
    #     :return: status
    #     """
    #     response = self._session.get(f'{self._url}/user/logout')
    #     return response.status_code
    #
    # def get_user_by_user_name(self, user_name: str) -> User:
    #     """
    #     :param user_name:
    #     :return: User
    #     """
    #     response = self._session.get(f'{self._url}/user/{user_name}')
    #     return User(*response.json())
    #
    # def Update_user(self, user_info: User):
    #     """
    #     :param user_info:
    #     :param user_name_to_change:
    #     :return: status
    #     """
    #     user_data = user_info.to_json()
    #     res = self._session.put(url=f"{self._url}/{user_info.username}", data=user_data)
    #     return res
    #
    # def delete_username(self, username: str):
    #     """
    #     :param username:
    #     :return:
    #     """
    #     response = self._session.delete(f"{self._url}/{username}")
    #     return response




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


uesrs = Users(url)

U1 = User(**user_1)

print(uesrs.create_user(U1))


list_of_users = [user_1, user_2, user_3, user_4]




