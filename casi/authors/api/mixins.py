from rest_framework.exceptions import ValidationError

from casi.authors.models import Author


class AuthorValidationMixin:

    def validate_email(self, value: str):
        return value.strip().lower()

    def validate_orcid(self, value: str) -> str:
        if not value:
            return value

        qs = Author.objects.filter(orc_id=value)

        # Update da o'zini chiqarib tashlaydi
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise ValidationError("This ORCID is already registered.")
        return value
