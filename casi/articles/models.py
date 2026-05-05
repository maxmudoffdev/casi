from django.db import models

from casi.common.models import TimeStampModel
from casi.journals.models import Volume


# Create your models here.


class Article(TimeStampModel):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(
        ...
    )
    doi = models.CharField(blank=True,null=True)
    keys = models.ManyToManyField(
        "Keys",related_name='articles'
    )
    abstract = models.TextField(blank=True,null=True)
    article_view = models.PositiveIntegerField(default=0)
    article_download = models.PositiveIntegerField(default=0)
    language = models.CharField(max_length=10,default='uz')
    file = models.FileField(upload_to='articles/file/%Y/%m')
    pages = models.CharField(max_length=20, blank=True, null=True)
    volume = models.ForeignKey(Volume,on_delete=models.CASCADE,related_name='articles')
    status = models.CharField(max_length=20, default='draft')


class ArticleReferences(TimeStampModel):
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    reference_name = models.TextField()


class Keys(TimeStampModel):
    name = models.CharField(max_length=128)

