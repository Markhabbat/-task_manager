from rest_framework import serializers

from tasks.models import Task
from tasks.tasks import send_mail_task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            "id",
            "title",
            "description",
            "created_by",
            "assigned_to",
        )

    def create(self, validated_data):
        instance = super().create(validated_data)
        if instance.assigned_to:
            send_mail_task.delay(instance.assigned_to.email, instance.id)
        return instance

    def update(self, instance, validated_data):
        previous = instance.assigned_to
        instance = super().update(instance, validated_data)
        if previous != instance.assigned_to:
            send_mail_task.delay(instance.assigned_to.email, instance.id)
        return instance
