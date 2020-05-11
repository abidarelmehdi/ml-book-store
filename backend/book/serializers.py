from rest_framework import serializers
from category.serializers import CategorySerializer
from author.serializers import AuthorSerializer
from book.models import Book


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "subtitle",
            "isbn",
            "publisher",
            "pages",
            "description",
            "thumbnail",
            "language",
            "avg_ratings",
            "raters",
            "authors",
            "categories",
        )
