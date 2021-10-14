from django.http.response import Http404
from django.db.utils import IntegrityError
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from apps.profiles.serializers import (
    FollowedSerializer,
    FollowingSerializer,
    ProfileActionsSerializer,
)
from apps.users.models import User, UserFollowing
from apps.users.serializers import UserSerializer


class ProfileDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @staticmethod
    def get_profile(pk):
        try:
            profile = User.objects.get(pk=pk)
            if not profile.is_active:
                raise User.DoesNotExist

            return profile

        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        profile = self.get_profile(pk)

        serializer = UserSerializer(profile)
        return Response(serializer.data)

    def post(self, request, pk):
        action_serializer = ProfileActionsSerializer(data=request.data)
        profile = self.get_profile(pk)

        if not action_serializer.is_valid():
            return Response(
                action_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        action = action_serializer.data["action"]

        if action == "follow":
            try:
                following = UserFollowing(
                    user_id=profile, following_user_id=request.user
                )

                following.save()

            except IntegrityError:
                pass

        elif action == "unfollow":
            following = UserFollowing.objects.filter(
                user_id=profile, following_user_id=request.user
            )

            following.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def get_followers(request, pk):
    profile = ProfileDetail.get_profile(pk)
    followers = UserFollowing.objects.filter(user_id=profile)
    serializer = FollowedSerializer(followers, many=True)

    return Response(serializer.data)


@api_view(["GET"])
def get_following(request, pk):
    profile = ProfileDetail.get_profile(pk)
    followers = UserFollowing.objects.filter(following_user_id=profile)
    serializer = FollowingSerializer(followers, many=True)

    return Response(serializer.data)
