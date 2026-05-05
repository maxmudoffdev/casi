from django.db import models
from casi.common.models import TimeStampModel
from casi.journals.models import Volume


class Category(TimeStampModel):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Keys(TimeStampModel):
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Keyword'
        verbose_name_plural = 'Keywords'

    def __str__(self):
        return self.name


class Article(TimeStampModel):
    title = models.CharField(max_length=256)
    doi = models.CharField(max_length=100, blank=True, null=True)
    abstract = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=10, default='uz')
    file = models.FileField(upload_to='articles/file/%Y/%m')
    pages = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=20, default='draft')
    article_view = models.PositiveIntegerField(default=0)
    article_download = models.PositiveIntegerField(default=0)
    volume = models.ForeignKey(
        Volume,
        on_delete=models.CASCADE,
        related_name='articles'
    )
    author = models.ManyToManyField(
        'authors.Author',
        related_name='articles'
    )
    keys = models.ManyToManyField(Keys, related_name='articles')
    category = models.ManyToManyField(Category, related_name='articles')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title


class ArticleReferences(TimeStampModel):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='references'
    )
    reference_name = models.TextField()

    class Meta:
        verbose_name = 'Article Reference'
        verbose_name_plural = 'Article References'

    def __str__(self):
        return self.reference_name
