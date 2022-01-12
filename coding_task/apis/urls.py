from django.urls import path

from coding_task.apis.views import (
    AckermannFunctionV1APIView,
    FibonacciSequenceV1APIView,
    FibonacciSequenceV2APIView,
)

app_name = "apis"
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

ackermann_urlpatterns = [
    path(
        "ackermann-function/v1/<str:m>/<str:n>/",
        AckermannFunctionV1APIView.as_view(),
        name="ackermann-function-v1",
    ),
]

urlpatterns = fibonacci_urlpatterns + ackermann_urlpatterns
