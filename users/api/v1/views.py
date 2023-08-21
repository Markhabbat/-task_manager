from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import PermissionDenied
from rest_framework.viewsets import ModelViewSet

from utils.permissions import IsAdministrator, IsAdministratorOrChangeRead
from users.api.v1.serializers import RoleSerializer, UserSerializer
from users.models import Role, User


class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = ModelViewSet.permission_classes + [IsAdministrator]


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = ModelViewSet.permission_classes + [IsAdministratorOrChangeRead]

    def get_queryset(self):
        queryset = super().get_queryset()
        if self._has_permission():
            return queryset
        return queryset.filter(pk=self.request.user.id)

    def update(self, request, *args, **kwargs):
        # Not Administrator users are able to change their own data except their Role,
        # To prevent the user from changing his role to have other accesses
        if not self._has_permission() and request.data.get('role', None):
            raise PermissionDenied(_('You do not have permission to change role.'))
        return super().update(request, *args, **kwargs)

    def _has_permission(self):
        return IsAdministrator().has_permission(self.request, self)
