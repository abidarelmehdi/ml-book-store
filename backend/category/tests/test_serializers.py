from django.test import TestCase
from category.serializers import CategorySerializer
from category.models import Category


class CompanySerializer(TestCase):
    def test_model_fields(self):
        """Serializer data matches the Category object for each field."""

        # arrange
        category = Category.objects.create(label="History")
        test_fields = ("id", "label")
        serializer = CategorySerializer(category)

        # test
        for field_name in test_fields:
            self.assertEqual(
                serializer.data[field_name], str(getattr(category, field_name))
            )
