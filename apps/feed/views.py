from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.tweets.models import Tweet
from apps.tweets.serializers import TweetSerializer
from apps.users.models import UserFollowing


@api_view(["GET"])
def global_feed(request):
    tweets = Tweet.objects.all()
    serializer = TweetSerializer(tweets, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def followers_feed(request):
    following_ids = UserFollowing.objects.filter(
        following_user_id=request.user
    ).values_list("user_id")

    print(following_ids)

    tweets = Tweet.objects.filter(owner__in=following_ids)
    serializer = TweetSerializer(tweets, many=True)

    return Response(serializer.data)
