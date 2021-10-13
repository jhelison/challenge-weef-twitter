from rest_framework import fields, serializers
from apps.users.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "name"]
