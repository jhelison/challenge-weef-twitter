from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.tweets.models import Tweet
from apps.tweets.serializers import TweetSerializer


@api_view(["GET"])
def global_feed(request):
    tweets = Tweet.objects.all()
    serializer = TweetSerializer(tweets, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def followers_feed(request):
    tweets = Tweet.objects.followers_feed(request.user)
    serializer = TweetSerializer(tweets, many=True)

    return Response(serializer.data)
