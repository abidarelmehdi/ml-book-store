from django.urls import include, path
from rest_framework.routers import DefaultRouter
from book.api import BookViewSet, RecommendedBooksListView, BookRatings
from book import views

app_name = "books"
router = DefaultRouter()
router.register("", BookViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("rating", BookRatings.as_view(), name="rate_book",),
    path("rating/<str:isbn>", BookRatings.as_view(), name="rate_book",),
    path(
        "recommend/content-based/<str:isbn>",
        RecommendedBooksListView.as_view(),
        name="recommended_view",
    ),
    path(
        "train/content-based",
        views.TrainContentBasedModel.as_view(),
        name="content_based_training",
    ),
    path("load_data", views.load_data, name="load_data")
    # path('', include('django.contrib.auth.urls'))
]
