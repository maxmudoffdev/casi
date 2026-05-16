from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter
from django.urls import path, include


from casi.users.api.views import UserViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)


app_name = "api"
urlpatterns = router.urls

urlpatterns += [
    path("authors/",include("casi.authors.api.urls")),
    path("journals/", include("casi.journals.api.urls")),
    path("submission/", include("casi.submission.api.urls")),
    path("reviews/", include("casi.reviews.api.urls")),
]



