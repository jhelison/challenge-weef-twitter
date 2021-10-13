from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class AccountManager(BaseUserManager):
    def create_user(self, email, name=None, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(email=self.normalize_email(email), name=name)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=self.normalize_email(email), password=password)
        user.is_superuser = True
        user.save(using=self._db)


class Users(AbstractBaseUser):
    email = models.EmailField(verbose_name="email")
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    objects = AccountManager()

    def __str__(self):
        return str(f"{self.email} | {self.name}")
