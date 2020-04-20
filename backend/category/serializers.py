from rest_framework import serializers
from category.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "label",
            "creation_by",
            "update_by",
            "creation_date",
            "update_date",
            "is_active",
        )
