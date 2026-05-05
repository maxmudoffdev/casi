from django.db import models

from casi.common.models import TimeStampModel


# Create your models here.
class Journal(TimeStampModel):
    name = models.CharField(max_length=200,unique=True)
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='journal/image',blank=True,null=True)
    logo = models.ImageField(upload_to='journal/logo',blank=True,null=True)
    issn = models.CharField(max_length=9,blank=True,null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Journal'
        verbose_name_plural = 'Journals'


class JournalRequirements(TimeStampModel):
    journal = models.OneToOneField(Journal,on_delete=models.CASCADE,related_name='requirements')
    content = models.JSONField(default=dict)



class Volume(TimeStampModel):
    journal = models.ForeignKey(
        Journal,on_delete=models.CASCADE,
        related_name='volumes'
    )
    number = models.IntegerField(max_length=128)
    issue = models.CharField(max_length=20)
    year = models.IntegerField()
    published_date = models.DateField(blank=True,null=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        unique_together = ['journal','number','issue','year']
        ordering = ['-year', '-number']

    def __str__(self):
        return f"{self.journal.name} {self.number} № {self.issue} ({self.year})"


