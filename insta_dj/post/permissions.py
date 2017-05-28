from rest_framework import permissions


class PostPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user
