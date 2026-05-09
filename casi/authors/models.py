import uuid
from django.core.validators import validate_email
from django.db import models

from casi.authors.manager import AuthorActivatinManager
from casi.authors.validators.validators import valideate_firstname, valideate_lastname, validate_affilation, \
    validate_orcid
from casi.common.models import TimeStampModel
from django.contrib.postgres.indexes import GinIndex
# Create your models here.


class Author(TimeStampModel):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    first_name = models.CharField(max_length=200,validators=[valideate_firstname])
    last_name = models.CharField(max_length=200,validators=[valideate_lastname])
    affiliation = models.CharField(max_length=200,validators=[validate_affilation])
    email = models.EmailField(unique=True,validators=[validate_email])
    orc_id = models.CharField(max_length=19,blank=True,null=True,unique=True,validators=[validate_orcid])
    is_active = models.BooleanField(default=True)
    objects = AuthorActivatinManager()

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




