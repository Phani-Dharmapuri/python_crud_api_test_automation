import pytest
from utils.api_helper import ApiHelper
import config

@pytest.fixture(scope="module")
def api():
    return ApiHelper(config.BASE_URL)

def test_create_user(api):
    data = {"name": "Test User", "job": "Developer"}
    response = api.create_user(data)
    assert response.status_code == 201
    assert response.json()["name"] == data["name"]
    assert response.json()["job"] == data["job"]
    global user_id
    user_id = response.json()["id"]

def test_get_user(api):
    user_id = 2  # Existing user ID in Reqres
    response = api.get_user(user_id)
    assert response.status_code == 200
    assert "id" in response.json()["data"]
    assert response.json()["data"]["id"] == user_id

def test_update_user(api):
    user_id = 2  # Existing user ID in Reqres
    updated_data = {"name": "Updated User", "job": "Senior Developer"}
    response = api.update_user(user_id, updated_data)
    assert response.status_code == 200
    assert response.json()["name"] == updated_data["name"]
    assert response.json()["job"] == updated_data["job"]

def test_delete_user(api):
    user_id = 2  # Existing user ID in Reqres
    response = api.delete_user(user_id)
    assert response.status_code == 204
