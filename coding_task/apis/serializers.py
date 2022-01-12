from rest_framework import serializers


class InputSerializer(serializers.Serializer):
    """
    Input serializer to receive and validate the n value.
    """

    n = serializers.IntegerField(min_value=0)
