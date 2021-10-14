from django.urls import path
from apps.feed import views

urlpatterns = [
    path("global", views.global_feed),
    path("followers", views.followers_feed),
]
