from django.db import models

from casi.common.models import TimeStampModel
from casi.users.models import User


# Create your models here.


class Author(TimeStampModel):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    affiliation = models.CharField(max_length=200)
    email = models.EmailField(blank=True,null=True)
    orc_id = models.CharField(max_length=19,blank=True,null=True,unique=True)

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

