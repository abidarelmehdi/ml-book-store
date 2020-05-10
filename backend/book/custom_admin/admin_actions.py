from core.ai_models.content_based import CosineSimilarityModel


def train_content_based_model(modeladmin):
    CosineSimilarityModel(train=True)


train_content_based_model.short_description = "Train the content based ML model"
