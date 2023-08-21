from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User


class Task(models.Model):
    title = models.CharField(
        _("title"),
        max_length=255,
    )
    description = models.CharField(
        _("description"),
        max_length=255,
        blank=True,
    )
    created_by = models.ForeignKey(
        User,
        models.SET_NULL,
        verbose_name=_("created_by"),
        blank=True,
        null=True,
    )
    assigned_to = models.ForeignKey(
        User,
        models.SET_NULL,
        verbose_name=_("assigned_to"),
        blank=True,
        null=True,
        related_name="+"
    )

    class Meta:
        verbose_name = _("task")
        verbose_name_plural = _("tasks")

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        print('****************************************')
        print(self.__dict__)
        instance = super().save(force_insert, force_update, using, update_fields)
        print(instance.__dict__)
        return instance
