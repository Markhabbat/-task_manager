from rest_framework.routers import SimpleRouter

from users.api.v1.views import RoleViewSet, UserViewSet


router = SimpleRouter()
router.register('users', UserViewSet)
router.register('roles', RoleViewSet)

urlpatterns = router.urls
