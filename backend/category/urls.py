from django.urls import include, path
from rest_framework.routers import DefaultRouter
from category.api import CategoryViewSet

app_name = "categories"
router = DefaultRouter()
router.register("", CategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
