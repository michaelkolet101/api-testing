import json
from pet_store.data.tags import *
from pet_store.data.pet import Pet
from pet_store.data.baseObj import *
import logging
import requests
from pet_store.data.generat_string import g_s
import random
import sys

url = "https://petstore3.swagger.io/api/v3"
if len(sys.argv) > 1:
    url = sys.argv[1]


class PetApi:

    status = {"available": "available", "pending": "pending", "sold": "sold"}

    def __init__(self, url: str):
        self._url = "https://petstore3.swagger.io/api/v3"
        self._headrs = {'accept': 'application/json'}
        self._session = requests.session()
        self._session.headers = self._headrs

    def get_pet_ById(self, pet_id: int) -> Pet:
        response = self._session.get(f"{self._url}/pet/{pet_id}")
        return Pet(**response.json())


    def get_pet_ById_status(self, pet_id: int) -> int:
        response = self._session.get(f"{self._url}/pet/{pet_id}")
        return response.status_code

    def add_new_pet(self, new_pet: Pet) -> int:
        """
        :param new_pet:
        :return:status
        """
        logging.info(type(new_pet))
        pet_data = new_pet.to_json()
        response = self._session.post(f"{self._url}/pet", data=pet_data)
        return response.status_code

    def update_pet_by_id(self, pet_id: int, new_data: json):
        """
        :param pet_id:
        :return: statuscode
        """
        response = self._session.put(url=f"{self._url}/pet/{pet_id}", data=new_data)
        return response.status_code

    def find_by_status(self, _status) -> [Pet]:
        """
        :param _status:
        :return:json data
        """
        response = self._session.get(f"{self._url}/pet/findByStatus?status={self.status[_status]}")
        return Pet(**response.json())


    def get_pet_by_tags(self, tags: Tags) -> [Pet]:
        tagsString = f'tags={tags[0]}'
        if not isinstance(tags, list):
            raise TypeError("tags must be a list of strings!")
        if len(tags) > 1:
            for tag in range(1, len(tags)):
                if not isinstance(tags[tag], str):
                    raise TypeError("one or more of the tags is not a string!")
                tagsString += f'&tags={tags[tag]}'
        res = self._session.get(url=f"{self._url}/pet/findByTags?{tagsString}")
        return res

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
        response = self._session.post(f"{self._url}/pet/{pet_id}?name={new_name}&status={new_status}")
        return response.status_code

    def delete_pet_by_id(self, pet_id: str):
        """
        :param pet_id:
        :return:status
        """
        response = self._session.delete(f"https://petstore3.swagger.io/api/v3/pet/{pet_id}")
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


# pet_1 = {
#             "id": random.randint(0, 1000000),
#             "name": g_s(),
#             "category": {"id": 3, "name": "Dragon"},
#             "photoUrls": ["string"],
#             "tags": [{"id": 200, "name": "jonson"}],
#             "status": "available"
#         }




