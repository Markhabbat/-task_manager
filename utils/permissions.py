from rest_framework.permissions import BasePermission, SAFE_METHODS

from utils.constants import ADMINISTRATOR


class IsAdministrator(BasePermission):
    """
    Allows access only to Administrator users.
    """
    def has_permission(self, request, view):
        user = request.user
        if user.is_superuser:
            return True
        return bool(user and hasattr(user, 'role') and user.role and user.role.name == ADMINISTRATOR)


class IsAdministratorOrChangeRead(IsAdministrator):
    """
    The user is Administrator, or request is a read-only.
    """
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS + ('PUT', 'PATCH') or
            super().has_permission(request, view)
        )
