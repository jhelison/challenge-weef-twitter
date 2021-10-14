from django.db import models
from django.db.models.query_utils import Q

from apps.users.models import User, UserFollowing


class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey("Tweet", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"TweetLike {self.id} = {self.user.name} | {self.tweet}"


class TweetQuerySet(models.QuerySet):
    def followers_feed(self, user):
        following_ids = UserFollowing.objects.filter(
            following_user_id=user
        ).values_list("user_id")

        return self.filter(Q(owner__in=following_ids) | Q(owner=user)).distinct()


class TweetManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return TweetQuerySet(self.model, using=self._db)

    def followers_feed(self, user):
        return self.get_queryset().followers_feed(user)


class Tweet(models.Model):
    parent = models.ForeignKey("Tweet", null=True, on_delete=models.SET_NULL)
    content = models.CharField(max_length=280)
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(
        User, related_name="tweet_user", blank=True, through=TweetLike
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    objects = TweetManager()

    def __str__(self):
        content = self.content[0:50] + "..." if len(self.content) > 50 else self.content
        return f"Tweet {self.id} = {self.owner} | {content}"

    def count_likes(self):
        return self.likes.all().count()

    class Meta:
        ordering = ["-created_at"]
