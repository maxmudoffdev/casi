from django.db import models

from casi.common.models import TimeStampModel
from casi.reviews.api.validators import validate_time_zone
from casi.reviews.validators import validate_comment, validate_file
from casi.submission.models import Submission
from casi.users.models import User


# Create your models here.


class ReviewRecommendation(models.TextChoices):
    ACCEPT  = "accept","ACCEPT"
    REJECT = "reject","REJECT"
    MAJOR_REVISION = "major_revision","MAJOR REVISION"
    MINOR_REVISION = "minor_revision", "Minor Revision"


class Review(TimeStampModel):
    submission = models.ForeignKey(Submission,on_delete=models.CASCADE, related_name="reviews")
    reviewer = models.ForeignKey(User,on_delete=models.CASCADE, related_name="reviews")
    comment = models.TextField(validators=[validate_comment])
    recommendation = models.CharField(max_length=20,choices=ReviewRecommendation.choices)
    is_submitted   = models.BooleanField(default=False)
    file = models.FileField(upload_to="reviews/file",blank=True,null=True,validators=[validate_file])

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["submission", "reviewer"]
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def __str__(self):
        return f"{self.reviewer} - {self.submission.title}"



class AssigmentStatus(models.TextChoices):
    PENDING = "pending", "Pending"
    ACCEPTED = "accepted", "Accepted"
    DECLINED = "declined", "Declined"
    COMPLETED = "completed", "Completed"



class ReviewAssigment(TimeStampModel):
    submission = models.ForeignKey(Submission,on_delete=models.CASCADE,related_name="assignments")
    reviewer = models.ForeignKey(Review,on_delete=models.CASCADE,related_name="assignments")
    asigment_by =models.ForeignKey(User,on_delete=models.CASCADE,related_name="assignments")

    deadline = models.DateField(validators=[validate_time_zone])
    status = models.CharField(
        max_length=20,
        choices=AssigmentStatus.choices,
        default=AssigmentStatus.PENDING
    )

    class Meta:
        unique_together = ["submission", "reviewer"]
        ordering = ["-created_at"]
        verbose_name = "Reviewer Assignment"
        verbose_name_plural = "Reviewer Assignments"

    def __str__(self):
        return f"{self.reviewer} → {self.submission.title}"






