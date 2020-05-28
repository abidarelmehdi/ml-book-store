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
        "recommend/content-based/<str:isbn>",
        api.RecommendedBooksListView.as_view(),
        name="recommended_view",
    ),
    path(
        "train/content-based",
        views.TrainContentBasedModel.as_view(),
        name="content_based_training",
    ),
    path("refresh", views.RefreshBooks.as_view(), name="refresh_books",),
    path("load_data", views.load_data, name="load_data")
    # path('', include('django.contrib.auth.urls'))
]
