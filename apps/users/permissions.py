from rest_framework import permissions


class IsSuperUser(permissions.BasePermission):
    """
        SuperUser permission
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_superuser

SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']
class IsManager(permissions.BasePermission):
    """
        SuperUser permission
    """

    def has_permission(self, request, view):
        if request.method not in SAFE_METHODS:
            return request.user and request.user.is_manager
        return bool(request.user)