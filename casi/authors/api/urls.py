from django.urls import path

from casi.authors.api.views import AllAuthorView,AuthorDetailView,DowloadAllUserView

urlpatterns = [
    path("",AllAuthorView.as_view()),
    path("<uuid:id>/", AuthorDetailView.as_view()),
    path("download/", DowloadAllUserView.as_view())
]
