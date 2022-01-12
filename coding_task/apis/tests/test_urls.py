from django.urls import reverse


class TestFibonacciSequenceUrls:
    """
    Test class for all tests related to fibonacci sequence apis urls.
        1) For v1 api, the url should be valid if n is given as a parameter in the path.
        2) For v2 api, the url should be valid if n is given as a parameter in the path.
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
