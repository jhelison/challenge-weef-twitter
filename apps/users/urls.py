from django.urls import path
from .views import signin, login, logout

urlpatterns = [
    path("signin/", signin),
    path("login/", login),
    path("logout/", logout),
]
