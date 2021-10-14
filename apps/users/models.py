from django.db import models

from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)


class AccountManager(BaseUserManager):
    def create_user(self, email, name=None, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(email=self.normalize_email(email), name=name)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, password):
        user = self.create_user(
            name=name, email=self.normalize_email(email), password=password
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)


class UserFollowing(models.Model):
    user_id = models.ForeignKey(
        "User", related_name="following", on_delete=models.CASCADE
    )
    following_user_id = models.ForeignKey(
        "User", related_name="followers", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        unique_together = (("user_id", "following_user_id"),)

    def __str__(self):
        return f"{self.user_id.email} | {self.following_user_id.email}"


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="email", unique=True)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    objects = AccountManager()

    def __str__(self):
        return str(f"{self.email} | {self.name}")

    def count_followers(self):
        return UserFollowing.objects.filter(user_id=self).count()

    def count_following(self):
        return UserFollowing.objects.filter(following_user_id=self).count()
