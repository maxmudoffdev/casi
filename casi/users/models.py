from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import  models

from casi.common.models import TimeStampModel
from casi.users.api.validators import validate_first_name, validate_last_name, validate_email


class UserRole(models.TextChoices):
    AUTHOR   = "author",   "Muallif"
    EDITOR   = "editor",   "Muharrir"
    REVIEWER = "reviewer", "Taqrizchi"
    ADMIN    = "admin",    "Admin"


class VerificationMethod(models.TextChoices):
    EMAIL    = "email",    "Email"
    TELEGRAM = "telegram", "Telegram"

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser,TimeStampModel):
    username = None
    first_name = models.CharField(max_length=200,blank=True,null=True,validators=[validate_first_name])
    last_name = models.CharField(max_length=200,blank=True,null=True,validators=[validate_last_name])
    email = models.EmailField(unique=True,validators=[validate_email])
    verification_method = models.CharField(
        max_length=20,
        choices=VerificationMethod.choices,
        default=VerificationMethod.TELEGRAM
    )
    role = models.CharField(max_length=20,choices=UserRole.choices,default=UserRole.AUTHOR)
    # Verification
    verification_token = models.CharField(max_length=100, blank=True, null=True)
    verification_token_expires = models.DateTimeField(blank=True, null=True)
    # Telegram
    telegram_chat_id = models.CharField(max_length=50, blank=True, null=True)
    telegram_token = models.CharField(max_length=50, blank=True, null=True)
    telegram_token_expires = models.DateTimeField(blank=True, null=True)
    telegram_verification_code = models.CharField(max_length=6, blank=True, null=True)
    telegram_code_expires = models.DateTimeField(blank=True, null=True)
    telegram_verified = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = UserManager()


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []



    def __str__(self):
        return self.email











