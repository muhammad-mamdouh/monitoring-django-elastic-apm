from django.urls import include, path

from .swagger import swagger_urlpatterns

urlpatterns = [
    path("apis/", include("coding_task.apis.urls", namespace="apis")),
]

urlpatterns += swagger_urlpatterns
