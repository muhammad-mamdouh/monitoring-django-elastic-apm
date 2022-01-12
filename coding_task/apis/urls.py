from django.urls import path

from coding_task.apis.views import (
    FibonacciSequenceV1APIView,
    FibonacciSequenceV2APIView,
)

app_name = "apis"
urlpatterns = [
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
