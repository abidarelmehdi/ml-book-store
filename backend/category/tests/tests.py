from django.test import TestCase
from django.db import IntegrityError
from category.models import Category


class CategoryTest(TestCase):
    """ Test module for Category model """

    def setUp(self):
        Category.objects.create(label="Fantasy")

    def test_category_label(self):
        fantasy_category = Category.objects.get(label="Fantasy")
        self.assertEqual(fantasy_category.label, "Fantasy")

    def test_unique_label(self):
        with self.assertRaises(IntegrityError):
            Category.objects.create(label="Fantasy")
