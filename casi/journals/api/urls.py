from  django.urls import  path

from casi.journals.api.view import AllJournalView,JournalDetailView

urlpatterns = [
    path("",AllJournalView.as_view()),
    path("<slug:slug>/", JournalDetailView.as_view())
]
