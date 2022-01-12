from django.urls import reverse


class TestFibonacciSequenceUrls:
    """
    Test class for all tests related to fibonacci sequence apis urls.
        1) For v1 api, the url should be valid if n is given as an argument in the path.
        2) For v2 api, the url should be valid if n is given as an argument in the path.
    """

    def test__fibonacci_sequence_v1_url__with_valid_n__should_be_valid_url(
        self,
        n_random_input_number: int,
    ) -> None:
        # Act
        reversed_url = reverse(
            "apis:fibonacci-sequence-v1", kwargs={"n": n_random_input_number}
        )
        expected_url = f"/apis/fibonacci-sequence/v1/{n_random_input_number}/"

        # Assert
        assert reversed_url == expected_url

    def test__fibonacci_sequence_v2_url__with_valid_n__should_be_valid_url(
        self,
        n_random_input_number: int,
    ) -> None:
        # Act
        reversed_url = reverse(
            "apis:fibonacci-sequence-v2", kwargs={"n": n_random_input_number}
        )
        expected_url = f"/apis/fibonacci-sequence/v2/{n_random_input_number}/"

        # Assert
        assert reversed_url == expected_url


class TestAckermannFunctionUrls:
    """
    Test class for all tests related to ackermann function apis urls.
        1) For v1 api, the url should be valid if m & n is given as arguments in the path.
        2) For v2 api, the url should be valid if m & n is given as arguments in the path.
    """

    def test__ackermann_function_v1_url__with_valid_m_and_n__should_be_valid_url(
        self,
        m_random_input_number: int,
        n_random_input_number: int,
    ) -> None:
        # Act
        reversed_url = reverse(
            "apis:ackermann-function-v1",
            kwargs={"m": m_random_input_number, "n": n_random_input_number},
        )
        expected_url = f"/apis/ackermann-function/v1/{m_random_input_number}/{n_random_input_number}/"

        # Assert
        assert reversed_url == expected_url

    def test__ackermann_function_v2_url__with_valid_m_and_n__should_be_valid_url(
        self,
        m_random_input_number: int,
        n_random_input_number: int,
    ) -> None:
        # Act
        reversed_url = reverse(
            "apis:ackermann-function-v2",
            kwargs={"m": m_random_input_number, "n": n_random_input_number},
        )
        expected_url = f"/apis/ackermann-function/v2/{m_random_input_number}/{n_random_input_number}/"

        # Assert
        assert reversed_url == expected_url
