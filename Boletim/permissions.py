from rest_framework import permissions


class IsAdminOrAccountOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        elif request.user.is_authenticated and request.user.is_superuser:
            return True

        else:
            return True
