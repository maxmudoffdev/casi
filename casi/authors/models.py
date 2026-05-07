import uuid
from django.db import models
from casi.common.models import TimeStampModel
from django.contrib.postgres.indexes import GinIndex

# Create your models here.


class Author(TimeStampModel):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    affiliation = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    orc_id = models.CharField(max_length=19,blank=True,null=True,unique=True)

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        indexes = [
            GinIndex(
                fields=["first_name","last_name"],
                name="author_full_name_trgm_idx",
                opclasses=['gin_trgm_ops','gin_trgm_ops']
            ),
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"




