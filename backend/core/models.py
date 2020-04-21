import uuid

from django.db import models
from django.utils import timezone

from django_currentuser.db.models import CurrentUserField


class CoreModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = CurrentUserField(
        related_name="created_by_%(app_label)s_%(class)ss", editable=False,
    )
    updated_by = CurrentUserField(
        related_name="updated_by_%(app_label)s_%(class)ss", editable=False,
    )
    creation_date = models.DateTimeField(
        verbose_name="Creation date", default=timezone.now, editable=False,
    )
    update_date = models.DateTimeField(
        verbose_name="Update date", auto_now=True, editable=False,
    )
    is_active = models.BooleanField("Is active ?", default=True)

    class Meta:
        abstract = True
