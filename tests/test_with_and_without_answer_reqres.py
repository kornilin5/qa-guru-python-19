import requests

DOMAIN_URL = 'https://reqres.in/api'
USER_URL = DOMAIN_URL + '/users'


def test_without_answer():
    response = requests.get(url=DOMAIN_URL + '/unknown/23')
    assert response.json() == {}
    assert response.status_code == 404


def test_with_answer():
    response = requests.get(url=DOMAIN_URL + '/unknown/2')
    assert response.json()["data"]["id"] == 2
    assert response.status_code == 200
