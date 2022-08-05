import json
import requests
import sys


class PetApi:

    status = {"available": "available", "pending": "pending", "sold": "sold"}

    def __init__(self, url: str):
        self._url = url
        self._headrs = {'accept': 'application/json'}
        self._session = requests.session()
        self._session.headers = self._headrs

    def get_pet_ById(self, _id: int):
        response = self._session.get(f"{self._url}/pet/{_id}")
        if response.status_code == 404:
            return "pet not pound"
        return response.json()

    def get_pet_ById_status(self, _id: int):
        response = self._session.get(f"{self._url}/pet/{_id}")
        return response.status_code

    def add_new_pet(self, new_pet: json):
        """
        :param new_pet:
        :return:status
        """
        response = self._session.post(f"{self._url}/pet", data=new_pet)
        return response.status_code

    def update_pet_by_id(self, pet_id: int, new_data: dict):
        """
        :param pet_id:
        :return: statuscode
        """
        response = self._session.put(url=f"{self._url}/pet", data=new_data)
        return response.status_code

    def find_by_status(self, _status):
        """
        :param _status:
        :return:json data
        """
        response = self._session.get(f"{self._url}/pet/findByStatus?status={self.status[_status]}")
        return response.json()

# TODO ask for help
    def find_by_tags(self, tags: dict):
        """
        :param tags:
        :return: status
        """
        response = self._session.get(f"{self._url}/pet/findByStatus?tags={(tags)}")
        return response.status_code

    def update_pet_by_id_post(self, pet_id: int, new_name: str, new_status):
        """
        :param pet_id:
        :param new_name:
        :param new_status:
        :return: status
        """
        new_data = self.get_pet_ById(pet_id)
        new_data['name'] = new_name
        new_data['status'] = new_status
        response = self._session.post(f"{self._url}/pet/100?name={new_name}&status={new_status}")
        return response.status_code

    def delete_pet_by_id(self, pet_id: int):
        """
        :param pet_id:
        :return:status
        """
        response = self._session.delete(f"{self._url}/pet/{pet_id}")
        return response.status_code

    def upload_image_by_id(self, pet_id: int, image: str):
        """
        :param pet_id:
        :param image:
        :return: status
        """
        response = self._session.post(f"{self._url}/pet/{pet_id}/uploadImage", headers={'Content-Type': 'application/octet-stream'}, data=image)
        return response.status_code


cat_category = {"id": 2, "name": "Cats"}

url = 'https://petstore3.swagger.io/api/v3'
# sys.argv[1]

pet_1 = {
            "id": 100,
            "name": "max",
            "category": {"id": 3, "name": "Dragon"},
            "photoUrls": ["string"],
            "tags": [{"id": 200, "name": "jonson"}],
            "status": "available"
        }
pet_2 = {
            "id": 101,
            "name": "maxima",
            "category": {"id": 1, "name": "Dog"},
            "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "string"}],
            "status": "available"
        }
pet_3 = {
            "id": 102,
            "name": "dana",
            "category": {"id": 4, "name": "Snake"},
            "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "string"}],
            "status": "available"
        }
pet_4 = {
            "id": 100,
            "name": "dana",
            "category": {"id": 4, "name": "Snake"},
            "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "string"}],
            "status": "available"
        }
pet_5 = {
            "id": 103,
            "name": "donald",
            "category": {"id": 4, "name": "dak"},
            "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "string"}],
            "status": "available"
        }





pet_store = PetApi(url)

print('add_new_pet', pet_store.add_new_pet(pet_1))
print(pet_store.get_pet_ById(100))
pet_1['name'] = 'MAXA!!!'
print(pet_store.update_pet_by_id(100, pet_1))
print(pet_store.get_pet_ById(100))
print(pet_store.find_by_status("available"))
print(pet_store.find_by_tags(pet_1['tags']))

print(pet_store.upload_image_by_id(100, 'jjj.jpg'))