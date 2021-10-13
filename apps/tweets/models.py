from django.db import models

from apps.users.models import User


class Tweet(models.Model):
    parent = models.ForeignKey("Tweet", null=True, on_delete=models.SET_NULL)
    content = models.CharField(max_length=280)
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(
        User, related_name="tweet_user", blank=True, through="TweetLike"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        content = self.content[0:50] + "..." if len(self.content) > 50 else self.content
        return f"{self.owner} | {content}"


class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
