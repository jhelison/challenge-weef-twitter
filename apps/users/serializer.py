from rest_framework import fields, serializers
from apps.users.models import User


class SignInSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "name", "password"]
