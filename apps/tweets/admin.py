from django.contrib import admin
from apps.tweets.models import Tweet, TweetLike

admin.site.register(Tweet)
admin.site.register(TweetLike)
