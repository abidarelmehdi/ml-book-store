from django.db import models
from django.conf import settings
from core.models import CoreModel
from core.custom.model_fields import TitleCharField


class Book(CoreModel):
    title = TitleCharField("Title", max_length=120)
    description = models.TextField("Description")
    thumbnail = models.ImageField(
        "Thumbnail", upload_to="thumbnails/%Y/%m/%d", null=True, blank=True
    )
    book = models.FileField("File", upload_to="books/%Y/%m/%d")
    authors = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="books"
    )

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return self.title
