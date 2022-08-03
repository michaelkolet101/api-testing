import requests
import sys

class Store:

    def __init__(self, url: str):
        self._url = url
        self._headrs = {'accept': 'application/json'}
        self._session = requests.session()
        self._session.headers = self._headrs


    def get_inventory(self):
        """
        :return:status
        """
        response = self._session.get(f"{self._url}/store/inventory")
        return response.status_code

    def add_new_order(self, order: dict):
        """
        :param order: dict with the order details
        :return:
        """
        response = self._session.post(f"{self._url}/store/order", data=order)
        return response.status_code

    def find_order_by_id(self, order_id: int):
        """
        :param order_id:
        :return: json with the order or status in fail
        """
        response = self._session.get(f"{self._url}/store/order/{order_id}")
        status = response.status_code
        if status != 200:
            return status
        return response.json()

    def delete_order_by_id(self, order_id):
        response = self._session.delete(f"{self._url}/store/order/{order_id}")
        return response.status_code


order_1 = {
    "id": 11,
    "petId": 198772,
    "quantity": 7,
    "shipDate": "2022-08-01T14:16:51.403Z",
    "status": "approved",
    "complete": True
}

order_2 = {
    "id": 12,
    "petId": 100,
    "quantity": 17,
    "shipDate": "2022-09-01T14:16:51.403Z",
    "status": "approved",
    "complete": True
}

order_3 = {
    "id": 13,
    "petId": 101,
    "quantity": 1,
    "shipDate": "2022-09-05T14:16:51.403Z",
    "status": "approved",
    "complete": True
}

url = 'https://petstore3.swagger.io/api/v3'
my_store = Store(url)


print(my_store.get_inventory())
print(my_store.add_new_order(order_1))
print(my_store.find_order_by_id(11))
print(my_store.delete_order_by_id(10))