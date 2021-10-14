from django.urls import path

from apps.users import views

urlpatterns = [
    path("signin/", views.signin),
    path("login/", views.login),
    path("logout/", views.logout),
]
