from django.urls import include, path
from rest_framework.routers import DefaultRouter
from author.api import AuthorViewSet

app_name = "authors"
router = DefaultRouter()
router.register("", AuthorViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
