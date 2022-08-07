import requests
import json
from generat_string import g_s

class Account:

    def __init__(self, url: str):
        self._url = url
        self._headrs = {'accept': 'application/json'}
        self._session = requests.session()
        self.headers = {
            'accept': 'application/json',
            'authorization': 'Basic b21lcm1hem9yMTI6T21lcjEyMyE==true',
            #'Authorization': f'Bearer {self.token}'
        }
        self._session.headers = self._headrs

    def Authorized(self, login_info: json):
        """
        :param login_info
        :return: status
        """
        response = self._session.post(f'{self._url}/Authorized', data=login_info)
        return response.json()

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

    def add_user_account_get_id(self, login_info: json):
        """
        :param login_info
        :return:json
        """
        response = self._session.post(f'{self._url}/User', data=login_info)
        return response.json()

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
        return response.json()


ac_1 = {
  "userName": g_s(),
  "password": "1234QW!ERreww"
}


acuont = Account('https://bookstore.toolsqa.com/Account/v1')


def main():

    user_id = acuont.add_user_account_get_id(ac_1)
    print(user_id)
    print(ac_1)
    print(acuont.Generate_token(ac_1))
    print(acuont.Authorized(ac_1))
    print(acuont.get_user_by_id(user_id))
    print('get_user_by_id',acuont.get_user_by_id(10))
    print(acuont.delete_user_by_id(user_id))
    # print(acuont.Authorized(ac_3))
    # print(acuont.Generate_token(ac_1))
    # print(acuont.add_user_account(ac_3))
    # print(acuont.delete_user_by_id('6535c7f8-997f-4494-8898-16d3f6461ea5'))
    # print(acuont.get_user_by_id('6535c7f8-997f-4494-8898-16d3f6461ea5'))

if __name__ == "__main__":
    main()