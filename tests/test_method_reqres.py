import requests
from conftest import  USER_URL

def test_get_users():
    response = requests.get(url=USER_URL, params={'page': 2})

    assert response.json()['total_pages'] == 2
    assert response.status_code == 200


def test_create_user():
    payload = {'name': 'Alex', 'job': 'Qa'}
    response = requests.post(url=USER_URL, json=payload)

    assert response.status_code == 201
    assert response.json()['name'] == 'Alex'
    assert response.json()["job"] == "Qa"


def test_update_user():
    payload = {'name': 'Alex', 'job': 'QaEngineer'}
    response = requests.put(url=USER_URL + '/2', json=payload)

    assert response.status_code == 200
    assert response.json()["job"] == "QaEngineer"


def test_delete_user():
    response = requests.delete(url=USER_URL + '/2')

    assert response.status_code == 204
