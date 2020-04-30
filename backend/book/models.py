from django.db import models
from langdetect import detect
from core.models import CoreModel
from core.custom.model_fields import TitleCharField, UpperCharField
from author.models import Author
from category.models import Category


class Book(CoreModel):
    title = TitleCharField("Title", max_length=250)
    subtitle = TitleCharField("Sub-Title", max_length=250)
    isbn = UpperCharField("ISBN", max_length=30)
    description = models.TextField("Description", null=True, blank=True)
    thumbnail = models.ImageField(
        "Thumbnail", upload_to="thumbnails/%Y/%m/%d", null=True, blank=True
    )
    authors = models.ManyToManyField(Author, related_name="books")
    categories = models.ManyToManyField(Category, related_name="books")
    language = models.CharField("Language", max_length=2, default="en")

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.language = self.title and detect(self.title)
        return super().save(*args, **kwargs)
