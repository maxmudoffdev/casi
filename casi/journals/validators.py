from casi.authors.validators.func import chek_not_none_or_emppty,check_short,check_not_xss,check_number_or_letter
import re
from django.core.exceptions import ValidationError

def validate_name(value:str) -> None:
    chek_not_none_or_emppty(value,"Name")
    check_short(value,"Name")
    check_not_xss(value,"Name")
    check_number_or_letter(value,"Nmae")



def validate_image_or_logo(image):
    max_image_size = 3 * 1024 * 1024
    if image.size > max_image_size:
        raise ValidationError(
            "Image size must be under 3MB.",
            code="image_too_large"
        )

    allowed_formats = ["jpg","jpeg","png","svg","heic","webp"]
    if image.name.split(".")[-1].lower() not in allowed_formats:
        raise ValidationError(
            f"Allowed formats: {', '.join(allowed_formats)}",
            code="invalid_image_format"
        )

def validate_issn(value:str) ->  None:
    pattern = r"^\d{4}-\d{3}[\dX]$"
    if not re.match(pattern,value):
        raise ValidationError(
            "Invalid ISSN format. Correct format: 1234-5678",
            code="invalid_issn"
        )

def validate_issue(value: str) -> None:
    # Raqam yoki maxsus nom
    pattern = r"^[\w\s\-]+$"
    if not re.match(pattern, value):
        raise ValidationError(
            "Invalid issue format.",
            code="invalid_issue"
        )
