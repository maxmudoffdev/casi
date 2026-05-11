from django.db import models
from casi.common.models import TimeStampModel
from casi.journals.validators import validate_name, validate_image_or_logo, validate_issn, validate_issue, \
    validate_requirements_content
from django.utils.text import slugify


# Create your models here.
class Journal(TimeStampModel):
    name = models.CharField(max_length=200,unique=True,validators=[validate_name])
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='journal/image',blank=True,null=True,validators=[validate_image_or_logo])
    logo = models.ImageField(upload_to='journal/logo',blank=True,null=True,validators=[validate_image_or_logo])
    issn = models.CharField(max_length=9,blank=True,null=True,unique=True,validators=[validate_issn])
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Journal'
        verbose_name_plural = 'Journals'

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args,**kwargs)



class JournalRequirements(TimeStampModel):
    journal = models.OneToOneField(Journal,on_delete=models.CASCADE,related_name='requirements')
    content = models.JSONField(default=dict,validators=[validate_requirements_content])

    def __str__(self):
        return  self.journal.name



class Volume(TimeStampModel):
    journal = models.ForeignKey(
        Journal,on_delete=models.CASCADE,
        related_name='volumes'
    )
    number = models.PositiveIntegerField()
    issue = models.CharField(max_length=20,validators=[validate_issue])
    year = models.PositiveIntegerField()
    published_date = models.DateField(blank=True,null=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        unique_together = ['journal','number','issue','year']
        ordering = ['-year', '-number']

    def __str__(self):
        return f"{self.journal.name} {self.number} № {self.issue} ({self.year})"


