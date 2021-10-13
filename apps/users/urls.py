from django.urls import path
from .views import sign_in, login, logout

urlpatterns = [
    path("sign-in/", sign_in),
    path("login/", login),
    path("logout/", logout),
]
