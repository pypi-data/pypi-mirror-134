from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import MainMenuItemViewSet, FlatMenuViewSet, RedirectPageApiView

app_name = "wagtailutils"

router = DefaultRouter()
router.register(r"menu", MainMenuItemViewSet)
router.register(r"flat-menu", FlatMenuViewSet)


urlpatterns = [
    path("menus/", include(router.urls)),
    path("redirects/", RedirectPageApiView.as_view(), name="redirects"),
]
