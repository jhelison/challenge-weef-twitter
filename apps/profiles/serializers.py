from rest_framework import serializers

from apps.users.serializers import UserSerializer
from apps.users.models import UserFollowing


PROFILE_ACTIONS = ["follow", "unfollow"]


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
