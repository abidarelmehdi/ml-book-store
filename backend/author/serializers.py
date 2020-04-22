from rest_framework import serializers
from author.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            "first_name",
            "last_name",
            "birthday",
            "picture",
            "gender",
            "twitter",
            "linkedin",
        )
