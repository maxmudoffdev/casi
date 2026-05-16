from django.urls import path
from casi.reviews.api.views import (AllReviewView,
                                    ReviewDetailView,
                                    SubmitView,
                                    ReviewAssigmentView,
                                    )

urlpatterns = [
    path("",AllReviewView.as_view()),
    path("review/assigment/", ReviewAssigmentView.as_view()),

    path("<uuid:id>/", ReviewDetailView.as_view()),
    path("<uuid:id>/submit/", SubmitView.as_view()),
    path("review/assigment/<uuid:id>/", SubmitView.as_view()),
]
