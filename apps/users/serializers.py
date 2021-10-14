from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from apps.users.models import User, UserFollowing

PROFILE_ACTIONS = ["follow", "unfollow"]


class UserSerializer(serializers.ModelSerializer):
    followers = serializers.IntegerField(source="count_followers", read_only=True)
    following = serializers.IntegerField(source="count_following", read_only=True)

    class Meta:
        model = User
        fields = ["id", "email", "name", "password", "followers", "following"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        if validated_data.get("password"):
            validated_data["password"] = make_password(validated_data["password"])

        user = User(**validated_data)
        user.save()

        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)


class ProfileActionsSerializer(serializers.Serializer):
    action = serializers.ChoiceField(choices=PROFILE_ACTIONS)


class FollowingSerializer(serializers.ModelSerializer):
    user_id = UserSerializer()

    class Meta:
        model = UserFollowing
        fields = ["user_id", "created_at"]


class FollowedSerializer(serializers.ModelSerializer):
    following_user_id = UserSerializer()

    class Meta:
        model = UserFollowing
        fields = ["following_user_id", "created_at"]
