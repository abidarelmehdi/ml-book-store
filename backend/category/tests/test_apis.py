from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from category.models import Category


class CategoryViewSetTestCase(TestCase):
    def setUp(self):
        self.list_url = reverse("categories:category-list")

    def get_detail_url(self, category_id):
        return reverse("categories:category-detail", kwargs={"pk": category_id})

    def test_get_list(self):
        """GET the list of Categories."""
        labels = ("Hisory", "Technology")
        self.categories = [
            Category.objects.create(label=labels[i]) for i in range(0, 2)
        ]
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            set(category["id"] for category in response.data),
            set(str(category.id) for category in self.categories),
        )

    def test_get_detail(self):
        """GET a detail page for a Category."""

        category = Category.objects.create(label="_Django Test")
        response = self.client.get(self.get_detail_url(str(category.id)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["label"], category.label)

    def test_post(self):
        """POST to create a Category."""

        data = {"label": "_LabelDjango_2"}
        ex_categories_count = Category.objects.count()
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), ex_categories_count + 1)

    def test_put(self):
        """PUT to update a Category."""

        category = Category.objects.create(label="_Django Test 003")
        data = {"label": "_Django Test 004"}
        response = self.client.put(
            self.get_detail_url(str(category.id)),
            data=data,
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # The object has really been updated
        category.refresh_from_db()
        for field_name in data.keys():
            self.assertEqual(getattr(category, field_name), data[field_name])

    def test_delete(self):
        """Delete Category"""

        category = Category.objects.create(label="_Django Test 004")
        response = self.client.delete(self.get_detail_url(str(category.id)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
