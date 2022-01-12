import logging

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from coding_task.apis.serializers import InputSerializer

LOGGER = logging.getLogger(__name__)


class FibonacciSequenceV1APIView(APIView):
    """
    API endpoint to return the nth term of Fibonacci Sequence.
    Version 1.

    :param int n: term for which the api will calculate the nth fibonacci sequence.
    :return int fibonacci_sequence: nth term of fibonacci sequence regarding the passed number.
    """

    # Swagger configs
    n_input_param = openapi.Parameter(
        "n",
        openapi.IN_PATH,
        description="Number for which the fibonacci sequence will be calculated.",
        type=openapi.TYPE_INTEGER,
    )

    def fibonacci_sequence(self, n: int) -> int:
        a, b = 0, 1

        for i in range(n):
            a, b = b, a + b

        return a

    @swagger_auto_schema(
        operation_summary="Fibonacci Sequence V1 API Endpoint",
        manual_parameters=[n_input_param],
        responses={
            status.HTTP_200_OK: "fibonacci_sequence: result",
            status.HTTP_400_BAD_REQUEST: "n: A valid integer is required.",
            status.HTTP_500_INTERNAL_SERVER_ERROR: "error: Sorry, we're facing internal errors 🤯 please try again!",
        },
    )
    def get(self, request, *args, **kwargs):
        n = self.kwargs.get("n")
        serializer = InputSerializer(data={"n": n})
        serializer.is_valid(raise_exception=True)

        try:
            result = self.fibonacci_sequence(serializer.validated_data["n"])
        except Exception as e:
            LOGGER.error(f"{self.__class__.__name__} | exception: {e.args}")
            return Response(
                {"error": "Sorry, we're facing internal errors 🤯 please try again!"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        return Response({"fibonacci_sequence": result}, status=status.HTTP_200_OK)


class FibonacciSequenceV2APIView(APIView):
    """
    API endpoint to return the nth term of Fibonacci Sequence.
    Version 2.
    Under development, please use version 1.

    :param int n: term for which the api will calculate the nth fibonacci sequence.
    :return int fibonacci_sequence: nth term of fibonacci sequence regarding the passed number.
    """

    @swagger_auto_schema(
        deprecated=True,
        operation_summary="Fibonacci Sequence V2 API Endpoint [DISABLED]",
        responses={
            status.HTTP_503_SERVICE_UNAVAILABLE: "notice: Version 2 is still under development 💻 please use version 1."
        },
    )
    def get(self, request, *args, **kwargs):

        return Response(
            {"notice": "Version 2 is still under development 💻 please use version 1."},
            status=status.HTTP_503_SERVICE_UNAVAILABLE,
        )
