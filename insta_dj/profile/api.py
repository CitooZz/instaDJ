from rest_framework import viewsets
from rest_framework import permissions

from django.contrib.auth.models import User

from account.serializers import (
    UserSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserSerializer
    queryset = User.objects.none()
