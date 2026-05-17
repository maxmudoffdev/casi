from django.urls import path
from casi.reviews.api.views import (AllReviewView,
                                    ReviewDetailView,
                                    SubmitView,
                                    ReviewAssigmentView,
                                    ReviewAssigmenDetailtView,
                                    AssignmentAcceptView,
                                    AssignmentDeclineView,
                                    AssignmentCompleteView,
                                    )

urlpatterns = [
    #Review
    path("",AllReviewView.as_view()),
    path("<uuid:id>/", ReviewDetailView.as_view()),
    path("<uuid:id>/submit/", SubmitView.as_view()),
    #Assigment
    path("assigment/", ReviewAssigmentView.as_view()),
    path("assigment/<uuid:id>/", ReviewAssigmenDetailtView.as_view()),
    path("assigment/<uuid:id>/accept/", AssignmentAcceptView.as_view()),
    path("assigment/<uuid:id>/decline/", AssignmentDeclineView.as_view()),
    path("assigment/<uuid:id>/complete/", AssignmentCompleteView.as_view()),
]
