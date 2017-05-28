from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route
from rest_framework import status
from django.contrib.auth.models import User

from .serializers import UserSerializer, FollowingSerializer


class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.none()

    @list_route(methods=['GET'])
    def followers(self, request):
        followers = User.objects.filter(profile__following=request.user)
        return Response(UserSerializer(followers, many=True).data)

    @list_route(methods=['GET'])
    def following(self, request):
        followings = User.objects.filter(profile__followers=request.user)
        return Response(UserSerializer(followings, many=True).data)

    @list_route(methods=['POST'])
    def follow(self, request):
        serializer = FollowingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.get(request.data.get('user'))
        request.user.profile.add(user)

        return Response(status=status.HTTP_200_OK)
