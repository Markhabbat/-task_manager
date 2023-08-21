from rest_framework.routers import SimpleRouter

from tasks.api.v1.views import TaskViewSet


router = SimpleRouter()
router.register('', TaskViewSet)

urlpatterns = router.urls
