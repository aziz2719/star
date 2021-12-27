from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="FLOWER-SHOP API",
        default_version="v1",
        description="API for FLOWER-SHOP",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="nursultandev@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

api_patterns = [
    # apps
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', include('users.urls')),
    path('posts/', include('posts.urls')),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(api_patterns)),
    path("auth/", include("rest_framework.urls")),

    # documentation
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc-ui"
    ),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)