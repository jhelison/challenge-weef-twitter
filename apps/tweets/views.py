from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from .serializers import TweetSerializer, TweetActionsSerializer
from .models import Tweet


# class FeedView(APIView):
#     def get(self, request):
#         tweets = Tweet.objects.all()
#         serializer = TweetSerializer(tweets, many=True)
#         return Response(serializer.data)


class TweetDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_tweet(self, pk):
        try:
            return Tweet.objects.get(pk=pk)
        except Tweet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        tweet = self.get_tweet(pk)

        if not tweet.is_active:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TweetSerializer(tweet)
        return Response(serializer.data)

    def delete(self, request, pk):
        tweet = self.get_tweet(pk)

        if tweet.owner != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        tweet.is_active = False
        tweet.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, pk):
        serializer = TweetActionsSerializer(data=request.data)
        if serializer.is_valid():
            return Response()

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
