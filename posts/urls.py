from posts import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("posts", views.PostView, basename="posts")
router.register("likes", views.LikeView, basename="likes")
urlpatterns = router.urls

