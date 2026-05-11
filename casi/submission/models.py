from django.db import models

from casi.authors.models import Author
from casi.common.models import TimeStampModel
from casi.journals.models import Journal, Volume
from casi.submission.validators import validate_title, validate_abstract, validate_cover_letter, validate_keyword, \
    validate_file
from casi.users.models import User


# Create your models here.


class SubmissionStatus(models.TextChoices):
    DRAFT              = "draft"
    SUBMITTED          = "submitted"
    UNDER_REVIEW       = "under_review"
    REVISION_REQUESTED = "revision_requested"
    RESUBMITTED        = "resubmitted"
    ACCEPTED           = "accepted"
    REJECTED           = "rejected"
    PUBLISHED          = "published"

class Submission(TimeStampModel):
    title = models.CharField(max_length=500,validators=[validate_title])
    abstract = models.TextField(validators=[validate_abstract])
    file = models.FileField(upload_to="submission/file",validators=[validate_file])
    keyword = models.JSONField(default=list,validators=[validate_keyword])
    journal = models.ForeignKey(Journal,on_delete=models.CASCADE)
    volume = models.ForeignKey(Volume,on_delete=models.CASCADE,blank=True,null=True)
    author = models.ManyToManyField(Author,blank=True,null=True)
    cover_letter = models.TextField(blank=True, null=True,validators=[validate_cover_letter])
    doi = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, choices=SubmissionStatus.choices, default=SubmissionStatus.DRAFT)
    submitted_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )



