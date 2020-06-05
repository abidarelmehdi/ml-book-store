from django.urls import include, path
from rest_framework.routers import DefaultRouter
from book import api
from book import views

app_name = "books"
router = DefaultRouter()
router.register("", api.BookViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("rating", api.BookRatings.as_view(), name="rate_book",),
    path("rating/<str:isbn>", api.BookRatings.as_view(), name="rate_book",),
    path(
        "user/ratings",
        api.UserRatedBookListView.as_view(),
        name="user_rated_books",
    ),
    path(
        "recommend/content-based/book/<str:isbn>",
        api.RecommendedBooksListView.as_view(),
        name="book_recommended_view",
    ),
    path(
        "recommend/content-based/user",
        api.UserRecommendedBooksListView.as_view(),
        name="user_recommended_view",
    ),
    path(
        "recommend/content-based/user/<int:user_id>",
        api.UserRecommendedBooksListView.as_view(),
        name="user_recommended_view_with_id",
    ),
    path(
        "train/content-based/cosine_similarity",
        views.CosineSimilarityContentBasedModel.as_view(),
        name="cosine_similarity_training",
    ),
    path(
        "train/content-based/user_preferences",
        views.UserPreferencesContentBasedModel.as_view(),
        name="user_preferences_training",
    ),
    path("refresh", views.RefreshBooks.as_view(), name="refresh_books",),
    path("load_data", views.load_data, name="load_data")
    # path('', include('django.contrib.auth.urls'))
]
