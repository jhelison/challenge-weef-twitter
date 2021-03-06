from django.contrib.auth.hashers import check_password
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from apps.users.models import User
from apps.users.serializers import (
    UserSerializer,
    LoginSerializer,
)


@api_view(["POST"])
def signin(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(email=serializer.data["email"])
        if not check_password(serializer.data["password"], user.password):
            raise IOError()
    except:
        return Response(
            "Email or password invalid.", status=status.HTTP_400_BAD_REQUEST
        )

    token = Token.objects.get_or_create(user=user)[0]

    return Response({"token": token.key}, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def logout(request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
