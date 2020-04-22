from django.contrib import admin
from author.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "birthday", "gender"]
    search_fields = ["first_name", "last_name"]
