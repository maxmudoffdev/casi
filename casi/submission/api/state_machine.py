from casi.submission.models import SubmissionStatus


ALLOWED_TRANSITIONS = {
    SubmissionStatus.DRAFT:[
        SubmissionStatus.SUBMITTED
    ],
    SubmissionStatus.SUBMITTED : [
        SubmissionStatus.UNDER_REVIEW,
        SubmissionStatus.DRAFT,

    ],
    SubmissionStatus.UNDER_REVIEW : [
        SubmissionStatus.REVISION_REQUESTED,
        SubmissionStatus.ACCEPTED,
        SubmissionStatus.REJECTED,
        SubmissionStatus.SUBMITTED,

    ],
    SubmissionStatus.REVISION_REQUESTED : [
        SubmissionStatus.RESUBMITTED
    ],
    SubmissionStatus.RESUBMITTED : [
        SubmissionStatus.UNDER_REVIEW
    ],
    SubmissionStatus.ACCEPTED : [
        SubmissionStatus.PUBLISHED
    ],
    SubmissionStatus.REJECTED: [],
    SubmissionStatus.PUBLISHED: [],
}


def transition_status(submission,new_status):
    allowed = ALLOWED_TRANSITIONS.get(submission.status,[])
    if new_status  not in allowed:
        raise ValueError(
            f"Cannot transition from '{submission.status}' to '{new_status}'. "
            f"Allowed transitions: {[s.value for s in allowed]}"
        )
    submission.status = new_status
    submission.save()
    return submission



