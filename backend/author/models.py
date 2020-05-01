from django.db import models
from core.models import CoreModel
from core.custom.model_fields import LowerCharField


class Author(CoreModel):
    name = LowerCharField("Name", max_length=250)
    bio = models.TextField("Biography", null=True, blank=True)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return f"{self.name}"
