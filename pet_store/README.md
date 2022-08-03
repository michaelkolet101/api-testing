# Pet Shop


### There are folders for each api with api and testes

###  All information is stored in the form of a dictionary and is sent as well

Examples for information:

####  
    pet_1 = {
            "id": 100,
            "name": "max",
            "category": {"id": 3, "name": "Dragon"},
            "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "string"}],
            "status": "available"
        }

#### 
    order_1 = {
        "id": 11,
        "petId": 198772,
        "quantity": 7,
        "shipDate": "2022-08-01T14:16:51.403Z",
        "status": "approved",
        "complete": True
    }

####  
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
###
### Running the code looks like this:
###
#### to run api:
path $ name_of_progarm.py
#####
The URL is hard coded
###
#### to run test:
pat $ pytest name_of_test.py 
#####
The URL is hard coded
