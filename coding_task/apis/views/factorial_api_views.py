import math
from decimal import Decimal

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from coding_task.apis.serializers import InputSerializer
from coding_task.apis.utils import endpoint_disabled_response

SWAGGER_DEF_N_INPUT_PARAM = openapi.Parameter(
    "n",
    openapi.IN_PATH,
    description="Number for which the factorial will be calculated.",
    type=openapi.TYPE_INTEGER,
)


class FactorialV1APIView(APIView):
    """
    API endpoint to calculate the factorial on n.
    Version 1.
    Implementation is with Stirling's approximation https://en.wikipedia.org/wiki/Stirling%27s_approximation
    to be able to calculate the large numbers and in a fast manner.

    :param int n: term for which the api will calculate the factorial.
    :return int approximate_factorial: approximate result of calculating the factorial on n.
    """

    def stirling_approximation_factorial(self, n):
        N = Decimal(n)
        return (Decimal(2 * math.pi) * N).sqrt() * (N / Decimal(math.e)) ** N

    @swagger_auto_schema(
        operation_summary="Factorial V1 API Endpoint",
        manual_parameters=[SWAGGER_DEF_N_INPUT_PARAM],
        responses={
            status.HTTP_200_OK: "approximate_factorial: result",
            status.HTTP_400_BAD_REQUEST: "n: A valid integer is required.",
        },
    )
    def get(self, request, *args, **kwargs):
        n = self.kwargs.get("n")
        serializer = InputSerializer(data={"n": n})
        serializer.is_valid(raise_exception=True)
        result = self.stirling_approximation_factorial(serializer.validated_data["n"])
        return Response({"approximate_factorial": result}, status=status.HTTP_200_OK)


class FactorialV2APIView(APIView):
    """
    API endpoint to calculate the factorial on n.
    Version 2.
    Under development, please use version 1.

    :param int n: term for which the api will calculate the factorial.
    :return int approximate_factorial: approximate result of calculating the factorial on n.
    """

    @swagger_auto_schema(
        deprecated=True,
        manual_parameters=[SWAGGER_DEF_N_INPUT_PARAM],
        operation_summary="Factorial V2 API Endpoint [DISABLED]",
        responses={
            status.HTTP_503_SERVICE_UNAVAILABLE: "notice: Version 2 is still under development 💻 please use version 1."
        },
    )
    def get(self, request, *args, **kwargs):
        return endpoint_disabled_response()
