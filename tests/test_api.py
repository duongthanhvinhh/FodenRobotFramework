import pytest
from api.users_api import UsersAPI
from api.models.user_model import UserCreate, UserUpdate
from api.base_client import APIError


@pytest.fixture
def users_api():
    return UsersAPI()


def test_get_user(users_api):
    # Test getting a specific user
    user = users_api.get_user(1)
    assert user.id == 1
    assert user.name
    assert user.email


def test_get_all_users(users_api):
    # Test getting all users
    users = users_api.get_all_users()
    assert isinstance(users, list)
    assert len(users) > 0
    assert all(user.id for user in users)


def test_create_user(users_api):
    # Test creating a new user
    new_user = UserCreate(
        name="John Doe",
        username="johndoe",
        email="john@example.com"
    )
    created_user = users_api.create_user(new_user)
    assert created_user.name == new_user.name
    assert created_user.username == new_user.username
    assert created_user.email == new_user.email


def test_update_user(users_api):
    # Test updating a user
    update_data = UserUpdate(
        name="Updated Name",
        username="updateduser",
        email="updated@example.com"
    )
    updated_user = users_api.update_user(1, update_data)
    assert updated_user.name == update_data.name
    assert updated_user.username == update_data.username
    assert updated_user.email == update_data.email


def test_delete_user(users_api):
    # Test deleting a user
    response = users_api.delete_user(1)
    assert response.status_code == 200


def test_invalid_user_data():
    # Test data validation
    with pytest.raises(ValueError):
        UserCreate(
            name="A",  # too short
            username="b",  # too short
            email="invalid-email"  # invalid email format
        )


def test_api_error_handling(users_api):
    # Test handling of non-existent user
    with pytest.raises(APIError) as exc_info:
        users_api.get_user(9999)
    assert exc_info.value.status_code == 404 