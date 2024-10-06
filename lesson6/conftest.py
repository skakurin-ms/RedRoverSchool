import pytest
import requests
from data.urls import urls

@pytest.fixture
def get_token():
    credentials = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(urls.URL_TOKEN, json=credentials)
    print(response.json())
    return response.json()["token"]