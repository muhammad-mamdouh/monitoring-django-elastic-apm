import pytest
from rest_framework import exceptions

from coding_task.apis.serializers import InputSerializer


class TestInputSerializer:
    """
    Test class for all tests related to the Input Serializer.
        1) If n passed as an integer >= 0, the serializer should validate it successfully.
        2) If n passed as a string, the serializer should raise a validation error.
        3) If n passed as a negative integer, the serializer should raise a validation error.
        4) If n & m passed as integers >= 0, the serializer should validate them successfully.
        5) If m passed as a string, the serializer should raise a validation error.
        6) If m passed as a negative integer, the serializer should raise a validation error.
    """

    def test__inputserializer__with_valid_n__should_be_valid(
        self,
        n_random_input_number: int,
    ) -> None:
        # Arrange
        serializer = InputSerializer(data={"n": n_random_input_number})

        # Act
        serializer.is_valid(raise_exception=True)

        # Assert
        assert serializer.validated_data["n"] == n_random_input_number

    def test__inputserializer__with_invalid_n__should_raise_validation_error(
        self, dummy_string: str
    ) -> None:
        # Arrange
        serializer = InputSerializer(data={"n": dummy_string})

        # Act
        with pytest.raises(exceptions.ValidationError) as err_info:
            serializer.is_valid(raise_exception=True)

        # Assert
        assert err_info.type == exceptions.ValidationError
        assert err_info.value.args[0]["n"][0] == "A valid integer is required."

    def test__inputserializer__with_negative_n__should_raise_validation_error(
        self,
    ) -> None:
        # Arrange
        serializer = InputSerializer(data={"n": -1})

        # Act
        with pytest.raises(exceptions.ValidationError) as err_info:
            serializer.is_valid(raise_exception=True)

        # Assert
        assert err_info.type == exceptions.ValidationError
        assert (
            err_info.value.args[0]["n"][0]
            == "Ensure this value is greater than or equal to 0."
        )

    def test__inputserializer__with_valid_n_and_m__should_be_valid(
        self,
        n_random_input_number: int,
        m_random_input_number: int,
    ) -> None:
        # Arrange
        serializer = InputSerializer(
            data={"n": n_random_input_number, "m": m_random_input_number}
        )

        # Act
        serializer.is_valid(raise_exception=True)

        # Assert
        assert serializer.validated_data["n"] == n_random_input_number
        assert serializer.validated_data["m"] == m_random_input_number

    def test__inputserializer__with_invalid_m__should_raise_validation_error(
        self, n_random_input_number: int, dummy_string: str
    ) -> None:
        # Arrange
        serializer = InputSerializer(
            data={"n": n_random_input_number, "m": dummy_string}
        )

        # Act
        with pytest.raises(exceptions.ValidationError) as err_info:
            serializer.is_valid(raise_exception=True)

        # Assert
        assert err_info.type == exceptions.ValidationError
        assert err_info.value.args[0]["m"][0] == "A valid integer is required."

    def test__inputserializer__with_negative_m__should_raise_validation_error(
        self,
        n_random_input_number: int,
    ) -> None:
        # Arrange
        serializer = InputSerializer(data={"n": n_random_input_number, "m": -1})

        # Act
        with pytest.raises(exceptions.ValidationError) as err_info:
            serializer.is_valid(raise_exception=True)

        # Assert
        assert err_info.type == exceptions.ValidationError
        assert (
            err_info.value.args[0]["m"][0]
            == "Ensure this value is greater than or equal to 0."
        )
