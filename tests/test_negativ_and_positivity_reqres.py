import requests
from conftest import  USER_URL, DOMAIN_URL


def test_positive_authorization_user():
    payload = {"email": "alex@mail.ru", "password": "city123123"}
    response = requests.post(url=USER_URL + '/login', json=payload)

    assert response.status_code == 201


def test_negative_authorization_user():
    payload = {"email": "Alex@mail.ru"}
    response = requests.post(url=DOMAIN_URL + '/login', json=payload)
    
    assert response.status_code == 400
