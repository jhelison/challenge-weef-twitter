from django.urls import path
from .views import sign_in

urlpatterns = [path("sign-in/", sign_in)]
