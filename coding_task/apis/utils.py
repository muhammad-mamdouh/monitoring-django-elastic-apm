from rest_framework import status
from rest_framework.response import Response


def endpoint_disabled_response() -> Response:
    return Response(
        {"notice": "Version 2 is still under development 💻 please use version 1."},
        status=status.HTTP_503_SERVICE_UNAVAILABLE,
    )
