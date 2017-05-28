from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import list_route
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer
from .permissions import PostPermission


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, PostPermission]
    serializer_class = PostSerializer
    queryset = Post.objects.none()

    def get_queryset(self):
        return Post.objects.filter(creator=self.request.user)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    @list_route(methods=['GET'])
    def feeds(self, request):
        posts = Post.objects.filter(
            creator__in=request.user.profile.following.all())

        return Response(self.get_serializer(posts, many=True).data)
