import requests
import json

class Account:

    def __init__(self, url: str):
        self._url = url
        self._headrs = {'accept': 'application/json'}
        self._session = requests.session()
        self._session.headers = self._headrs

    def Authorized(self, login_info: json):
        """
        :param login_info
        :return: status
        """
        response = self._session.post(f'{self._url}/Authorized', data=login_info)
        return response.status_code

    def Generate_token(self, login_info: json):
        """
        :param login_info:
        :return: json
        """
        response = self._session.post(f'{self._url}/GenerateToken', data=login_info)
        return response.json()

    def add_user_account(self, login_info: json):
        """
        :param user_name:
        :param password:
        :return:json
        """
        response = self._session.post(f'{self._url}/User', data=login_info)
        return response.status_code

    def delete_user_by_id(self, user_id: str):
        """
        :param user_id:
        :return:status
        """
        response = self._session.delete(f'{self._url}/User/{user_id}')
        return response.status_code



    def get_user_by_id(self, user_id: str):
        """
        :param user_id:
        :return:json
        """
        response = self._session.get(f'{self._url}/User/{user_id}')
        return response.status_code


ac_1 = {
  "userName": "dani rop",
  "password": "1234QWEqwe!"
}

ac_2 = {
  "userName": "mic",
  "password": "1234QWEqwe!"
}

ac_3 = {
  "userName": "nama",
  "password": "1234QWEqwe!"
}

acuont = Account('https://bookstore.toolsqa.com/Account/v1')
print(acuont.Authorized(ac_1))
print(acuont.Generate_token(ac_1))
print(acuont.add_user_account(ac_3))
print(acuont.delete_user_by_id('6535c7f8-997f-4494-8898-16d3f6461ea5'))
print(acuont.get_user_by_id('6535c7f8-997f-4494-8898-16d3f6461ea5'))

