from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_time_zone(value):
    if value < timezone.now().date():
        raise ValidationError(
            "Deadline cannot be in the past",
            code="invalid_deadline"
        )


def validate_assignment(submission_id,review_id,assigned_by_id):
    from casi.reviews.models import ReviewAssigment

    if review_id == assigned_by_id:
        raise ValidationError(
            "Reviewer cannot assign themselves.",
            code="self_assignment"
        )
    if (ReviewAssigment
        .objects
        .filter(
        submission_id=submission_id,
        reviewer_id=review_id,
    ).exists()):
        raise ValidationError(
            "This reviewer is already assigned to this submission.",
            code="already_assigned"
        )



