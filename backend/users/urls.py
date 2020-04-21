from django.urls import include, path
from rest_framework.routers import DefaultRouter
from users.api import CustomUserViewSet

app_name = "users"
router = DefaultRouter()
router.register("", CustomUserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    # path('', include('django.contrib.auth.urls'))
]
