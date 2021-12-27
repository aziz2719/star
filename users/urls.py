from users import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("users", views.UserViewSet, basename="users")
urlpatterns = router.urls
