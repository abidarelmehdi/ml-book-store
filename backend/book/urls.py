from django.urls import include, path
from rest_framework.routers import DefaultRouter
from book.api import BookViewSet
from book import views

app_name = "books"
router = DefaultRouter()
router.register("", BookViewSet)

urlpatterns = [
    path("", include(router.urls)),
    # path("load_data", views.load_data, name="load_data")
    # path('', include('django.contrib.auth.urls'))
]
