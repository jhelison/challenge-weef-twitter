from rest_framework import serializers
from apps.tweets.models import Tweet

TWEET_ACTIONS = ["like", "retweet"]


class TweetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.id")

    class Meta:
        model = Tweet
        fields = ["id", "content", "created_at", "owner"]

    def create(self, validated_data):
        user = self.context["request"].user

        tweet = Tweet(**validated_data, owner=user)

        return tweet


class TweetActionsSerializer(serializers.Serializer):
    action = serializers.ChoiceField(choices=TWEET_ACTIONS)
    content = serializers.CharField(max_length=280, required=False)

    def validate(self, data):
        """
        Checks if the action is retweet, if so, requires a content.
        """
        if data["action"] == "retweet":
            if not data.get("content"):
                raise serializers.ValidationError("Content is required when retweeting")

        return data
