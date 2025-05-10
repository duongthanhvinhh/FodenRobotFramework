import json
from typing import Any, Optional, Type, TypeVar
import requests
from pydantic import BaseModel
from requests import Response
from requests.auth import AuthBase


T = TypeVar('T', bound=BaseModel)


class TokenAuth(AuthBase):
    def __init__(self, token: str):
        self.token = token

    def __call__(self, r):
        r.headers['Authorization'] = f'Bearer {self.token}'
        return r


class APIError(Exception):
    def __init__(self, message: str, status_code: int, response: Optional[Response] = None):
        self.message = message
        self.status_code = status_code
        self.response = response
        super().__init__(self.message)


class BaseAPIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.headers = {}
        self._auth_token = None

    def set_auth_token(self, token: str):
        """Set authentication token for subsequent requests."""
        self._auth_token = token
        self.session.auth = TokenAuth(token)

    def set_headers(self, headers: dict):
        self.headers.update(headers)
        self.session.headers.update(self.headers)

    def _handle_response(self, response: Response, expected_model: Optional[Type[T]] = None) -> Any:
        """Handle API response and validate against expected model if provided."""
        try:
            response.raise_for_status()
            if expected_model and response.content:
                data = response.json()
                if isinstance(data, list):
                    return [expected_model(**item) for item in data]
                return expected_model(**data)
            return response
        except requests.exceptions.HTTPError as e:
            raise APIError(
                message=f"HTTP Error: {str(e)}",
                status_code=response.status_code,
                response=response
            )
        except json.JSONDecodeError:
            raise APIError(
                message="Invalid JSON response",
                status_code=response.status_code,
                response=response
            )
        except Exception as e:
            raise APIError(
                message=f"Error processing response: {str(e)}",
                status_code=response.status_code if response else 0,
                response=response
            )

    def get(self, endpoint: str, params: dict = None, expected_model: Type[T] = None) -> Any:
        url = f"{self.base_url}{endpoint}"
        response = self.session.get(url, params=params)
        return self._handle_response(response, expected_model)

    def post(self, endpoint: str, json: dict = None, data: dict = None, expected_model: Type[T] = None) -> Any:
        url = f"{self.base_url}{endpoint}"
        response = self.session.post(url, json=json, data=data)
        return self._handle_response(response, expected_model)

    def put(self, endpoint: str, json: dict = None, expected_model: Type[T] = None) -> Any:
        url = f"{self.base_url}{endpoint}"
        response = self.session.put(url, json=json)
        return self._handle_response(response, expected_model)

    def delete(self, endpoint: str) -> Response:
        url = f"{self.base_url}{endpoint}"
        response = self.session.delete(url)
        return self._handle_response(response)

    def patch(self, endpoint: str, json: dict = None, expected_model: Type[T] = None) -> Any:
        url = f"{self.base_url}{endpoint}"
        response = self.session.patch(url, json=json)
        return self._handle_response(response, expected_model) 