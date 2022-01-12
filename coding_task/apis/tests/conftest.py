import random
import string
from typing import Callable, Union

import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.fixture
def api_client() -> APIClient:
    return APIClient()


@pytest.fixture
def m_random_input_number() -> int:
    return random.randint(0, 3)


@pytest.fixture
def n_random_input_number() -> int:
    return random.randint(0, 3)


@pytest.fixture
def dummy_string() -> str:
    return "".join(random.choice(string.ascii_lowercase) for _ in range(5))


@pytest.fixture
def make_fibonacci_api_call(api_client: APIClient):
    def _make_fibonacci_api_call(version_number: int, n: Union[int, str]) -> tuple:
        fibonacci_api_url = reverse(
            f"apis:fibonacci-sequence-v{version_number}", kwargs={"n": n}
        )
        response = api_client.get(fibonacci_api_url)
        json_response = response.json()
        return response, json_response

    return _make_fibonacci_api_call


@pytest.fixture
def make_ackermann_function_api_call(api_client: APIClient) -> Callable:
    def _make_ackermann_function_api_call(
        version_number: int, m: Union[int, str], n: Union[int, str]
    ) -> tuple:
        ackermann_api_url = reverse(
            f"apis:ackermann-function-v{version_number}", kwargs={"m": m, "n": n}
        )
        response = api_client.get(ackermann_api_url)
        json_response = response.json()
        return response, json_response

    return _make_ackermann_function_api_call
