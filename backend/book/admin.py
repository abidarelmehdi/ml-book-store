from django.contrib import admin
from book.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "subtitle",
        "publisher",
        "isbn",
        "pages",
        "language",
        "avg_ratings",
        "categories_as_text",
    ]
    search_fields = [
        "id",
        "title",
        "subtitle",
        "publisher",
        "isbn",
    ]
