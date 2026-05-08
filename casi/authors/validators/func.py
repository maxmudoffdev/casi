import re
from django.core.exceptions import ValidationError


def chek_not_none_or_emppty(value:str,field) -> None:
    if not value or not value.strip():
        raise ValidationError(f"{field} cannot be blank", code="blank_name")


def check_short(value:str,field) -> None:
    if len(value.strip()) < 2:
        raise ValidationError(f"{field} is short.", code="name_too_short")


def check_not_xss(value:str,field) -> None:
    pattern = r"[<>\"'&]"
    if re.search(pattern, value):
        raise ValidationError(
            f"{field} contains invalid characters",
            code="invalid_characters"
        )

def check_number_or_letter(value:str,field):
    if not re.match(r"^[a-zA-ZÀ-ÿА-яЁё\s'\-]+$", value):
        raise ValidationError(
            f"{field} must contain letters only.",
            code="invalid_name"
        )
