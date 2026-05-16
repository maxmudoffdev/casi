from django.urls import path

from casi.submission.api.view import (
    AllSubmissionView,
    SubmissionDetailView,
    SubmissionSubmitView,
    SubmissionUnderReviewView,
    SubmissionAcceptView,
    SubmissionRejectView,
    SubmissionRevisionView,
    SubmissionPublishView
)

urlpatterns = [
    path("",AllSubmissionView.as_view()),
    path("<uuid:id>/", SubmissionDetailView.as_view()),
    path("<uuid:id>/submit/", SubmissionSubmitView.as_view()),
    path("<uuid:id>/review/", SubmissionUnderReviewView.as_view()),
    path("<uuid:id>/accept/", SubmissionAcceptView.as_view()),
    path("<uuid:id>/reject/", SubmissionRejectView.as_view()),
    path("<uuid:id>/revision/", SubmissionRevisionView.as_view()),
    path("<uuid:id>/publish/", SubmissionPublishView.as_view()),
]
