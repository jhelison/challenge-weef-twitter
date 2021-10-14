from django.urls import path

from apps.profiles import views

urlpatterns = [
    path("<int:pk>", views.ProfileDetail.as_view()),
    path("<int:pk>/following", views.get_following),
    path("<int:pk>/followers", views.get_followers),
]
