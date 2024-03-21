import requests

DOMAIN_URL = 'https://reqres.in/api'
USER_URL = DOMAIN_URL + '/users'


def test_positive_autorization_user():
    payload = {"email": "alex@mail.ru", "password": "city123123"}
    response = requests.post(url=USER_URL + '/login', json=payload)

    assert response.status_code == 201


def test_negative_autorization_user():
    payload = {"email": "Alex@mail.ru"}
    response = requests.post(url=DOMAIN_URL + '/login', json=payload)
    assert response.status_code == 400
