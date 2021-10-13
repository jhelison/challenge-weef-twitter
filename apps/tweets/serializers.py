from django.db.models import fields
from django.utils.translation import activate
from rest_framework import serializers

from apps.tweets.models import Tweet

TWEET_ACTIONS = ["like", "retweet"]


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = "__all__"


class TweetActionsSerializer(serializers.Serializer):
    action = serializers.ChoiceField(choices=TWEET_ACTIONS)
    content = serializers.CharField(max_length=280)
