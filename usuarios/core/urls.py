from django.urls import path
from .views import RegistroAPIView, LoginAPIView

urlpatterns = [
    path("registro", RegistroAPIView.as_view(), name="registro"),
    path("login", LoginAPIView.as_view(), name="login"),
]