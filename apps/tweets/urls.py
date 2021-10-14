from django.urls import path

from apps.tweets import views

urlpatterns = [
    path("<int:pk>", views.TweetDetail.as_view()),
    path("<int:pk>/likes", views.list_likes),
    path("", views.create_tweet),
]
