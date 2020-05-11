from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter
from users.api import CustomUserViewSet

app_name = "users"
router = DefaultRouter()
router.register("", CustomUserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "token/obtain/",
        jwt_views.TokenObtainPairView.as_view(),
        name="token_obtain",
    ),
    path(
        "token/refresh/",
        jwt_views.TokenRefreshView.as_view(),
        name="token_refresh",
    ),
]
