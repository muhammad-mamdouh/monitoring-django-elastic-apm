from typing import Callable

import pytest
from rest_framework import status


@pytest.mark.django_db
class TestFibonacciSequenceAPIViews:
    """
    Test class for all tests related to fibonacci sequence api views.
        1) With valid integer n, fibonacci sequence api view v1 should return 200 ok.
        2) With string n, fibonacci sequence api view v1 should return 400 bad request.
        3) With negative n, fibonacci sequence api view v1 should return 400 bad request.
        4) Fibonacci sequence api view v2 should return 503 service unavailable with any n.
    """

    FIBONACCI_API_VERSION_1 = 1
    FIBONACCI_API_VERSION_2 = 2

    def test__fibonacci_api_view_v1__with_valid_n__should_return_valid_integer_with_200_ok(
        self, make_fibonacci_api_call: Callable, n_random_input_number: int
    ) -> None:
        # Act
        response, json_response = make_fibonacci_api_call(
            self.FIBONACCI_API_VERSION_1, n_random_input_number
        )

        # Assert
        assert response.status_code == status.HTTP_200_OK
        assert type(json_response.get("fibonacci_sequence")) is int

    def test__fibonacci_api_view_v1__with_string_n__should_return_400_bad_request(
        self, make_fibonacci_api_call: Callable, dummy_string: str
    ) -> None:
        # Act
        response, json_response = make_fibonacci_api_call(
            self.FIBONACCI_API_VERSION_1, dummy_string
        )

        # Assert
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert json_response.get("n")[0] == "A valid integer is required."

    def test__fibonacci_api_view_v1__with_negative_n__should_return_400_bad_request(
        self, make_fibonacci_api_call: Callable
    ) -> None:
        # Act
        response, json_response = make_fibonacci_api_call(
            self.FIBONACCI_API_VERSION_1, -1
        )

        # Assert
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert (
            json_response.get("n")[0]
            == "Ensure this value is greater than or equal to 0."
        )

    def test__fibonacci_api_view_v2__with_valid_n__should_return_service_unavailable(
        self, make_fibonacci_api_call: Callable, n_random_input_number: int
    ) -> None:
        # Act
        response, json_response = make_fibonacci_api_call(
            self.FIBONACCI_API_VERSION_2, n_random_input_number
        )

        # Assert
        assert response.status_code == status.HTTP_503_SERVICE_UNAVAILABLE
        assert (
            json_response.get("notice")
            == "Version 2 is still under development 💻 please use version 1."
        )


@pytest.mark.django_db
class TestAckermannFunctionAPIViews:
    """
    Test class for all tests related to ackermann function api views.
        1) with valid m & n, ackermann function api view v1 should return 200 ok.
        2) With string m or n, ackermann function api view v1 should return 400 bad request.
        3) With negative m or n, ackermann function api view v1 should return 400 bad request.
        4) Ackermann function api view v2 should return 503 service unavailable with any m & n.
    """

    ACKERMANN_API_VERSION_1 = 1
    ACKERMANN_API_VERSION_2 = 2

    def test__ackermann_api_view_v1__with_valid_m_and_n__should_return_valid_integer_with_200_ok(
        self,
        make_ackermann_function_api_call: Callable,
        m_random_input_number: int,
        n_random_input_number: int,
    ) -> None:
        # Act
        response, json_response = make_ackermann_function_api_call(
            self.ACKERMANN_API_VERSION_1, m_random_input_number, n_random_input_number
        )

        # Assert
        assert response.status_code == status.HTTP_200_OK
        assert type(json_response.get("ackermann")) is int

    def test__ackermann_api_view_v1__with_string_m__should_return_400_bad_request(
        self,
        make_ackermann_function_api_call: Callable,
        dummy_string: str,
        n_random_input_number: int,
    ) -> None:
        # Act
        response, json_response = make_ackermann_function_api_call(
            self.ACKERMANN_API_VERSION_1, dummy_string, n_random_input_number
        )

        # Assert
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert json_response.get("m")[0] == "A valid integer is required."

    def test__ackermann_api_view_v1__with_negative_m__should_return_400_bad_request(
        self, make_ackermann_function_api_call: Callable, n_random_input_number: int
    ) -> None:
        # Act
        response, json_response = make_ackermann_function_api_call(
            self.ACKERMANN_API_VERSION_1, -1, n_random_input_number
        )

        # Assert
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert (
            json_response.get("m")[0]
            == "Ensure this value is greater than or equal to 0."
        )

    def test__ackermann_api_view_v2__with_valid_m_and_n__should_return_service_unavailable(
        self,
        make_ackermann_function_api_call: Callable,
        m_random_input_number: int,
        n_random_input_number: int,
    ) -> None:
        # Act
        response, json_response = make_ackermann_function_api_call(
            self.ACKERMANN_API_VERSION_2, m_random_input_number, n_random_input_number
        )

        # Assert
        assert response.status_code == status.HTTP_503_SERVICE_UNAVAILABLE
        assert (
            json_response.get("notice")
            == "Version 2 is still under development 💻 please use version 1."
        )
