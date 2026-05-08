from django.db import models

class AuthorActivatinManager(models.Manager):
    """ soft delete method"""
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
