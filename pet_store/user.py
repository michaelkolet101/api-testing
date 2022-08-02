import json

import requests


class User:

    def __init__(self, url: str):
        self._url = url
        self._headrs = {'accept': 'application/json'}
        self._session = requests.session()
        self._session.headers = self._headrs

    def create_user(self, user_info: dict):
        response = self._session.post(f'{self._url}/user', data=user_info)
        return response.status_code

# TODO fix that
    def create_with_list(self, users_list: list):
        response = self._session.post(f'{self._url}/user/createWithList', data=users_list)
        return response.status_code

    def login(self, usr_name: str, password: str):
        """
        :param usr_name:
        :param password:
        :return: session id
        """
        response = self._session.get(f'{self._url}/user/login?username={usr_name}&password={password}')
        return response.text

    def logout(self):
        """
        logout
        :return: status
        """
        response = self._session.get(f'{self._url}/user/logout')
        return response.status_code

    def get_user_by_user_name(self, user_name):
        response = self._session.get(f'{self._url}/user/{user_name}')
        return response.text

    def Update_user(self, update: dict, usr_name: str):
        self.login('theUser', '12345')
        d = self.get_user_by_user_name('theUser')
        f = json.loads(d)
        f['firstName'] = 'dan'
        response = self._session.post('https://petstore3.swagger.io/api/v3/user/theUser', data=f)
        return response.text


users = User("https://petstore3.swagger.io/api/v3")

user_1 = {
  "id": 10,
  "username": "theUser!!!",
  "firstName": "John",
  "lastName": "James",
  "email": "john@email.com",
  "password": "12345",
  "phone": "12345",
  "userStatus": 1
}

user_2 = {
  "id": 100,
  "username": "theUser",
  "firstName": "Mich",
  "lastName": "Kolet",
  "email": "john@email.com",
  "password": "12345",
  "phone": "12345",
  "userStatus": 1
}

list_of_users = [user_1, user_2]
json_list = [json.dumps(item) for item in list_of_users]



print(list_of_users)
print(users.create_user(user_1))
print(users.create_with_list(str(list_of_users)))
print(users.logout())
print(users.get_user_by_user_name('theUser'))
print(users.Update_user(user_2, 'theUser'))