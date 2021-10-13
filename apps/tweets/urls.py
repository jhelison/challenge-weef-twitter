from django.urls import path
from apps.tweets import views

urlpatterns = [
    path("<int:pk>", views.TweetDetail.as_view()),
]
