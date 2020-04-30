from django.contrib import admin
from book.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = (
        "title",
        "subtitle",
        "isbn",
        "description",
        "thumbnail",
        "language",
        "authors",
        "categories",
    )
    autocomplete_fields = (
        "authors",
        "categories",
    )
