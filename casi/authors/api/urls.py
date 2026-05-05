from django.urls import path

from casi.authors.api.views import AllAuthorView,AuthorDetailView

urlpatterns = [
    path("",AllAuthorView.as_view()),
    path("<int:id>/", AuthorDetailView.as_view())
]
