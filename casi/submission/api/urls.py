from django.urls import path

from casi.submission.api.view import AllSubmissionView

urlpatterns = [
    path("",AllSubmissionView.as_view())
]
