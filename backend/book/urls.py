from django.urls import include, path
from rest_framework.routers import DefaultRouter
from book.api import BookViewSet

app_name = "books"
router = DefaultRouter()
router.register("", BookViewSet)

urlpatterns = [
    path("", include(router.urls)),
    # path('', include('django.contrib.auth.urls'))
]
