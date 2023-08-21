from django.db.models import Q
from rest_framework.viewsets import ModelViewSet

from tasks.api.v1.serializers import TaskSerializer
from tasks.models import Task


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            Q(created_by=self.request.user.id) |
            Q(assigned_to=self.request.user.id)
        )
