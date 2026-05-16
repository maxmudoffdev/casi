from django.core.exceptions import ValidationError

from casi.common.func import check_not_xss,chek_not_none_or_emppty


def validate_comment(value:str) -> None:
    chek_not_none_or_emppty(value,"Comment")
    check_not_xss(value,"Comment")

    if len(value) < 100:
        raise ValidationError(
            "Comment must be at least 100 characters.",
            code="invalid_comment"
        )



def validate_file(file):
    max_size = 10 * 1024 * 1024
    allowed_file = ["pdf","docx"]
    file_name = file.name.lower().split('.')[-1]
    if file.size > max_size:
        raise ValidationError("max file size 10mb",code="invalid_file_size")

    if file_name not in allowed_file:
        raise ValidationError("Your uploud only pdf or docx file",code="invalid_file_format")


