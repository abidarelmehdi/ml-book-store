from math import floor
from django.db import models
from django.contrib.auth import get_user_model
from core.models import CoreModel
from core.custom.model_fields import TitleCharField, UpperCharField
from author.models import Author
from category.models import Category

User = get_user_model()


class Book(CoreModel):
    title = TitleCharField("Title", max_length=250)
    subtitle = models.TextField("Sub-Title", null=True, blank=True)
    publisher = TitleCharField(
        "Publisher", max_length=250, null=True, blank=True
    )
    isbn = UpperCharField("ISBN", max_length=30, unique=True)
    pages = models.SmallIntegerField("Pages", null=True, blank=True)
    description = models.TextField("Description", null=True, blank=True)
    thumbnail = models.URLField(
        "Thumbnail", max_length=250, null=True, blank=True
    )
    authors = models.ManyToManyField(Author, related_name="books")
    categories = models.ManyToManyField(Category, related_name="books")
    ratings = models.ManyToManyField(
        User, through="UserRatings", related_name="books"
    )
    avg_ratings = models.SmallIntegerField("Rating", default=0)
    raters = models.BigIntegerField("Raters", default=0)
    language = models.CharField("Language", max_length=10, default="en")

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ["-raters"]

    def __str__(self):
        return self.title

    def categories_as_text(self):
        return " | ".join(self.categories.values_list("label", flat=True))

    def authors_as_text(self):
        return " | ".join(self.authors.values_list("label", flat=True))


class UserRatings(models.Model):
    book = models.ForeignKey(
        Book,
        related_name="user_ratings",
        to_field="isbn",
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User, related_name="user_ratings", on_delete=models.CASCADE
    )
    rate = models.SmallIntegerField("Rate")

    class Meta:
        indexes = [models.Index(fields=["user_id"])]

    def save(self, *args, **kwargs):
        created = True if not self.id else False
        super().save(*args, **kwargs)
        if created:
            # Update number of raters in book when user rate a book
            self.book.raters = self.book.user_ratings.count()
            self.book.avg_ratings = floor(
                self.book.user_ratings.aggregate(models.Avg("rate")).get(
                    "rate__avg"
                )
            )
            self.book.save()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        # Update number of raters and rate average in book when user rate a book
        self.book.raters = self.book.user_ratings.count()
        self.book.avg_ratings = floor(
            self.book.user_ratings.aggregate(models.Avg("rate")).get(
                "rate__avg"
            )
        )
        self.book.save()
