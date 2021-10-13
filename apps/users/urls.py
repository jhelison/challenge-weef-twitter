from django.urls import path
from apps.users import views

urlpatterns = [
    path("signin/", views.signin),
    path("login/", views.login),
    path("logout/", views.logout),
    path("profile/<int:pk>", views.ProfileDetail.as_view()),
    path("profile/<int:pk>/following", views.get_following),
    path("profile/<int:pk>/followers", views.get_followers),
]
