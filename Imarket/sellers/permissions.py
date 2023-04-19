from rest_framework import permissions
from .choices import Role


class IsSellerOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user
            and request.user.is_authenticated
            and request.user.user_type == Role.SELLER
        )
