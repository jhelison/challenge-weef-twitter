from rest_framework import fields, serializers
from apps.users.models import User
from django.contrib.auth.hashers import make_password


class SignInSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "name", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        if validated_data.get("password"):
            validated_data["password"] = make_password(validated_data["password"])

        user = User(**validated_data)
        user.save()

        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
