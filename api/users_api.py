from typing import List

from api.base_client import BaseAPIClient
from api.models.user_model import UserCreate, UserResponse, UserUpdate


class UsersAPI(BaseAPIClient):
    def __init__(self):
        # Example using JSONPlaceholder API
        super().__init__("https://jsonplaceholder.typicode.com")

    def get_user(self, user_id: int) -> UserResponse:
        return self.get(f"/users/{user_id}", expected_model=UserResponse)

    def get_all_users(self) -> List[UserResponse]:
        return self.get("/users", expected_model=UserResponse)

    def create_user(self, user_data: UserCreate) -> UserResponse:
        return self.post("/users", json=user_data.model_dump(), expected_model=UserResponse)

    def update_user(self, user_id: int, user_data: UserUpdate) -> UserResponse:
        return self.put(f"/users/{user_id}", json=user_data.model_dump(), expected_model=UserResponse)

    def delete_user(self, user_id: int):
        return self.delete(f"/users/{user_id}") 