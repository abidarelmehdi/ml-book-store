from django.db.models import Count
from core.ai_models.content_based import CosineSimilarityModel
from book.models import Book


def train_content_based_model(modeladmin):
    CosineSimilarityModel(train=True)


train_content_based_model.short_description = "Train the content based ML model"
