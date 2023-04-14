from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:  # if request is SAFE --> read-only, no changes
            return True

        return bool(request.user and request.user.is_staff)  # giving all permission for admin users


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, obj):
        if request.method and permissions.SAFE_METHODS:
            return True

        return obj.user == request.user
