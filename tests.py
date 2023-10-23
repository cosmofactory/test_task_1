"""
Тестовый модуль для работы с пользователями.

К сожалению схема в сваггере не всегда совпадала
 с реальным состоянием API. Поэтому пришлось прибегнуть
 к костылям в виде global. Нормальный формат pytest
 с fixtures не захотел работать сходу.
"""

import requests

API_BASE_URL = "http://195.2.75.92:58760/api"
USERNAME = "Madrid6"
PASSWORD = "Istanbul6"
EMAIL = "testuser21@example.com"


def test_created_user():
    global user_id
    response = requests.post(
        f"{API_BASE_URL}/users/",
        json={"email": EMAIL, "username": USERNAME, "password": PASSWORD},
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert "id" in data
    user_id = data["id"]


def test_token():
    global access_token
    response = requests.post(
        f"{API_BASE_URL}/auth/jwt/create/",
        json={"username": USERNAME, "password": PASSWORD},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert "access" in data
    access_token = data["access"]


def test_verify_token():
    response = requests.post(
        f"{API_BASE_URL}/auth/jwt/verify/", json={"token": access_token}
    )
    assert response.status_code == 200


def test_get_users():
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(f"{API_BASE_URL}/users/", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_get_user_by_id():
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(
        f"{API_BASE_URL}/users/{user_id}/", headers=headers
    )
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "username" in data
    assert data["id"] == user_id


def test_delete_user():
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.delete(
        f"{API_BASE_URL}/users/me/",
        headers=headers,
        json={"current_password": PASSWORD},
    )
    assert response.status_code == 204
