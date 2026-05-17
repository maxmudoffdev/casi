from casi.reviews.models import AssigmentStatus


ASSIGMENT_TRANSITIONS = {
    AssigmentStatus.PENDING: [
            AssigmentStatus.ACCEPTED,
            AssigmentStatus.DECLINED,
        ],
        AssigmentStatus.ACCEPTED: [
            AssigmentStatus.COMPLETED,
        ],
        AssigmentStatus.DECLINED: [],
        AssigmentStatus.COMPLETED: [],
}


def transition_assignment(assignment, new_status):
    allowed = ASSIGMENT_TRANSITIONS.get(assignment.status, [])

    if new_status not in allowed:
        raise ValueError(
            f"Cannot transition from '{assignment.status}' to '{new_status}'. "
            f"Allowed: {[s.value for s in allowed]}"
        )

    assignment.status = new_status
    assignment.save()
    return assignment
