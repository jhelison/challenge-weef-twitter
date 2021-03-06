from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, permission_classes

from apps.tweets.serializers import (
    TweetLikeSerializer,
    TweetSerializer,
    TweetActionsSerializer,
)
from apps.tweets.models import Tweet, TweetLike


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def create_tweet(request):
    serializer = TweetSerializer(data=request.data, context={"request": request})

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TweetDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @staticmethod
    def get_tweet(pk):
        try:
            tweet = Tweet.objects.is_active().get(pk=pk)
            return tweet

        except Tweet.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        tweet = self.get_tweet(pk)

        serializer = TweetSerializer(tweet)
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = TweetActionsSerializer(data=request.data)
        tweet = self.get_tweet(pk)

        if serializer.is_valid():
            action = serializer.data["action"]

            if action == "like":
                tweet.likes.add(request.user)
                return Response(status=status.HTTP_204_NO_CONTENT)

            elif action == "unlike":
                tweet.likes.remove(request.user)
                return Response(status=status.HTTP_204_NO_CONTENT)

            elif action == "retweet":
                new_tweet = Tweet(
                    parent=tweet,
                    content=serializer.data.get("content"),
                    owner=request.user,
                )
                new_tweet.save()

                tweet_serializer = TweetSerializer(new_tweet)
                return Response(tweet_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        tweet = self.get_tweet(pk)

        if tweet.owner != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        tweet.is_active = False
        tweet.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def list_likes(request, pk):
    likes = TweetLike.objects.filter(tweet=pk)

    serializer = TweetLikeSerializer(likes, many=True)

    return Response(serializer.data)
