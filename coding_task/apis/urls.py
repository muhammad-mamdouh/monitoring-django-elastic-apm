from django.urls import path

from coding_task.apis.views import (
    AckermannFunctionV1APIView,
    AckermannFunctionV2APIView,
    FactorialV1APIView,
    FibonacciSequenceV1APIView,
    FibonacciSequenceV2APIView,
)

app_name = "apis"
ackermann_urlpatterns = [
    path(
        "ackermann-function/v1/<str:m>/<str:n>/",
        AckermannFunctionV1APIView.as_view(),
        name="ackermann-function-v1",
    ),
    path(
        "ackermann-function/v2/<str:m>/<str:n>/",
        AckermannFunctionV2APIView.as_view(),
        name="ackermann-function-v2",
    ),
]

factorial_urlpatterns = [
    path(
        "factorial/v1/<str:n>/",
        FactorialV1APIView.as_view(),
        name="factorial-v1",
    ),
]

fibonacci_urlpatterns = [
    path(
        "fibonacci-sequence/v1/<str:n>/",
        FibonacciSequenceV1APIView.as_view(),
        name="fibonacci-sequence-v1",
    ),
    path(
        "fibonacci-sequence/v2/<str:n>/",
        FibonacciSequenceV2APIView.as_view(),
        name="fibonacci-sequence-v2",
    ),
]

urlpatterns = fibonacci_urlpatterns + ackermann_urlpatterns
