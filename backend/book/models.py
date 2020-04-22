from django.db import models
from core.models import CoreModel
from core.custom.model_fields import TitleCharField
from author.models import Author
from category.models import Category


class Book(CoreModel):
    title = TitleCharField("Title", max_length=120)
    description = models.TextField("Description", null=True, blank=True)
    thumbnail = models.ImageField(
        "Thumbnail", upload_to="thumbnails/%Y/%m/%d", null=True, blank=True
    )
    book = models.FileField("File", upload_to="books/%Y/%m/%d")
    authors = models.ManyToManyField(Author, related_name="books")
    categories = models.ManyToManyField(Category, related_name="books")

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return self.title
