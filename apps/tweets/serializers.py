from rest_framework import serializers
from apps.tweets.models import Tweet, TweetLike
from apps.users.serializers import UserSerializer


TWEET_ACTIONS = ["like", "unlike", "retweet"]


class TweetSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    likes = serializers.IntegerField(source="count_likes")

    class Meta:
        model = Tweet
        fields = ["id", "content", "created_at", "owner", "likes", "parent"]
        read_only_fields = ["likes"]

    def create(self, validated_data):
        user = self.context["request"].user

        tweet = Tweet(**validated_data, owner=user)
        tweet.save()

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


class TweetLikeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = TweetLike
        fields = ["user", "created_at"]
