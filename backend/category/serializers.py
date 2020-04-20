from rest_framework import serializers
from category.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "label",
            "created_by",
            "updated_by",
            "creation_date",
            "update_date",
            "is_active",
        )
