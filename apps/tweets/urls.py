from django.urls import path
from apps.tweets import views

urlpatterns = [
    path("<int:pk>", views.TweetDetail.as_view()),
    path("<int:pk>/likes", views.list_likes),
    path("feed/", views.FeedView.as_view()),
]
