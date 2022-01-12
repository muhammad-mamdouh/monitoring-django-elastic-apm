import pytest
from rest_framework import exceptions

from coding_task.apis.serializers import NInputSerializer


class TestNInputSerializer:
    """
    Test class for all tests related to the NInput Serializer.
        1) If n passed as an integer >= 0, the serializer should validate it successfully.
        2) If n passed as a string, the serializer should raise a validation error.
        3) If n passed as a negative integer, the serializer should raise a validation error.
    """

    def test__ninputserializer__with_valid_n__should_be_valid(
        self,
        n_random_input_number: int,
    ) -> None:
        # Arrange
        serializer = NInputSerializer(data={"n": n_random_input_number})

        # Act
        serializer.is_valid(raise_exception=True)

        # Assert
        assert serializer.validated_data["n"] == n_random_input_number

    def test__ninputserializer__with_invalid_n__should_raise_validation_error(
        self,
    ) -> None:
        # Arrange
        serializer = NInputSerializer(data={"n": "dummy string"})

        # Act
        with pytest.raises(exceptions.ValidationError) as err_info:
            serializer.is_valid(raise_exception=True)

        # Assert
        assert err_info.type == exceptions.ValidationError
        assert err_info.value.args[0]["n"][0] == "A valid integer is required."

    def test__ninputserializer__with_negative_n__should_raise_validation_error(
        self,
    ) -> None:
        # Arrange
        serializer = NInputSerializer(data={"n": -1})

        # Act
        with pytest.raises(exceptions.ValidationError) as err_info:
            serializer.is_valid(raise_exception=True)

        # Assert
        assert err_info.type == exceptions.ValidationError
        assert (
            err_info.value.args[0]["n"][0]
            == "Ensure this value is greater than or equal to 0."
        )
