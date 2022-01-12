from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from coding_task.apis.serializers import NInputSerializer


class FibonacciSequenceV1APIView(APIView):
    """
    API endpoint to return the nth term of Fibonacci Sequence.
    :param int n: term for which the api will calculate the nth fibonacci sequence.
    :return int fibonacci_sequence: nth term of fibonacci sequence regarding the passed number.
    """

    def fibonacci_sequence(self, n: int) -> int:
        a, b = 0, 1

        for i in range(n):
            a, b = b, a + b

        return a

    def get(self, request, *args, **kwargs):
        n = self.kwargs.get("n")
        serializer = NInputSerializer(data={"n": n})
        serializer.is_valid(raise_exception=True)

        try:
            result = self.fibonacci_sequence(serializer.validated_data["n"])
        except Exception as e:
            # TODO: log the error
            return Response({
                "error": "Sorry, we're facing internal errors 🤯 please try again!"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return Response({"fibonacci_sequence": result}, status=status.HTTP_200_OK)
