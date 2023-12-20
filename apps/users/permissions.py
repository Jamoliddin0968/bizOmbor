from rest_framework import permissions

class IsSuperUser(permissions.BasePermission):
    """
        SuperUser permission
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_superuser
