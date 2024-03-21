from jsonschema import validate
import requests
import json

DOMAIN_URL = 'https://reqres.in/api'
USER_URL = DOMAIN_URL + '/users'



def test_schema_get_users_validation():
    response = requests.get(url=USER_URL, params={"page": 2})
    shema = json.loads(open("utils/get_users.json").read())

    validate(response.json(), shema)


def test_shema_get_single_user_validation():
    response = requests.get(url=USER_URL, params={"id": 2})
    shema = json.loads(open("utils/get_single_user.json").read())

    validate(response.json(), shema)

def test_shema_get_resources_validation():
    response = requests.get(url=DOMAIN_URL + '/unknown')
    shema = json.loads(open("utils/get_resources.json").read())

    validate(response.json(), shema)
    
def test_shema_get_single_resource_validation():
    response = requests.get(url=DOMAIN_URL + '/unknown/2')
    shema = json.loads(open("utils/get_single_resource.json").read())

    validate(response.json(), shema)