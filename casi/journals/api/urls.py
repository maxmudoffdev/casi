from  django.urls import  path

from casi.journals.api.view import (
    AllJournalView,
    JournalDetailView,
    VolumeView,
    VolumeViewDetail,
    JournalRequirementsView,
    JournalRequirementsDetailView,
)

urlpatterns = [
    path("",AllJournalView.as_view()),
    path("volume/", VolumeView.as_view()),
    path("requirements/", JournalRequirementsView.as_view()),
    path("<slug:slug>/", JournalDetailView.as_view()),
    path("volume/<uuid:id>/", VolumeViewDetail.as_view()),
    path("requirements/<uuid:id>/", JournalRequirementsDetailView.as_view()),
]
