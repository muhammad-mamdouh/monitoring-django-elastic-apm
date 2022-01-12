import sys
from functools import lru_cache

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from coding_task.apis.serializers import InputSerializer


class AckermannFunctionV1APIView(APIView):
    """
    API endpoint to calculate the ackermann function given m and n.
    Version 1.
    :param int m: first param to calculate the ackermann function.
    :param int n: second param to calculate the ackermann function.
    :return int ackermann: the result of calculating the ackermann function for m and n.
    """

    # Swagger configs
    m_input_param = openapi.Parameter(
        "m",
        openapi.IN_PATH,
        description="First argument given to the Ackermann Function to be calculated.",
        type=openapi.TYPE_INTEGER,
    )
    n_input_param = openapi.Parameter(
        "n",
        openapi.IN_PATH,
        description="Second argument given to the Ackermann Function to be calculated.",
        type=openapi.TYPE_INTEGER,
    )

    @lru_cache(maxsize=None)
    def calculate_ackermann(self, m, n):
        if m == 0:
            return n + 1

        elif n == 0:
            return self.calculate_ackermann(m - 1, 1)

        else:
            return self.calculate_ackermann(m - 1, self.calculate_ackermann(m, n - 1))

    @swagger_auto_schema(
        operation_summary="Ackermann Function V1 API Endpoint",
        manual_parameters=[m_input_param, n_input_param],
        responses={
            status.HTTP_200_OK: "ackermann: result",
            status.HTTP_400_BAD_REQUEST: "m|n: A valid integer is required.",
            status.HTTP_500_INTERNAL_SERVER_ERROR: "error: Sorry, we're facing internal errors 🤯 please try again!",
        },
    )
    def get(self, request, *args, **kwargs):
        # Increase the recursion limit
        sys.setrecursionlimit(3_000_0)

        # Receive and validate m and n input values.
        m = self.kwargs.get("m")
        n = self.kwargs.get("n")
        serializer = InputSerializer(data={"m": m, "n": n})
        serializer.is_valid(raise_exception=True)

        try:
            result = self.calculate_ackermann(
                serializer.validated_data["m"], serializer.validated_data["n"]
            )
        except RecursionError as e:
            # TODO: log the error
            return Response(
                {"error": "Sorry, we're facing internal errors 🤯 please try again!"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        return Response({"ackermann": result}, status=status.HTTP_200_OK)


class AckermannFunctionV2APIView(APIView):
    """
    API endpoint to calculate the ackermann function given m and n.
    Version 2.
    Under development, please use version 1.
    :param int m: first param to calculate the ackermann function.
    :param int n: second param to calculate the ackermann function.
    :return int ackermann: the result of calculating the ackermann function for m and n.
    """

    @swagger_auto_schema(
        deprecated=True,
        operation_summary="Ackermann Function V2 API Endpoint [DISABLED]",
        responses={
            status.HTTP_503_SERVICE_UNAVAILABLE: "notice: Version 2 is still under development 💻 please use version 1."
        },
    )
    def get(self, request, *args, **kwargs):

        return Response(
            {"notice": "Version 2 is still under development 💻 please use version 1."},
            status=status.HTTP_503_SERVICE_UNAVAILABLE,
        )
