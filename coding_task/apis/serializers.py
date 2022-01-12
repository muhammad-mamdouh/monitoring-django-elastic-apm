from rest_framework import serializers


class InputSerializer(serializers.Serializer):
    """
    Input serializer to receive and validate the m and n values.
    """

    n = serializers.IntegerField(min_value=0)
    m = serializers.IntegerField(min_value=0, required=False)
