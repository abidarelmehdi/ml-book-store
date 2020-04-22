from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/users/", include("users.urls")),
    path("api/categories/", include("category.urls")),
    path("api/authors/", include("author.urls")),
    path("api/books/", include("book.urls")),
]
