from django.core.exceptions import ValidationError
from casi.common.func import check_not_xss,chek_not_none_or_emppty,check_short,check_number_or_letter

def validate_title(value:str) -> None:

    chek_not_none_or_emppty(value,"Title")
    if len(value) < 10 or len(value) > 500:
        raise ValidationError(
            "This field min 10 max 500",
            code="invalid_title"
        )
    check_not_xss(value,"Title")


def validate_abstract(value:str) -> None:
    chek_not_none_or_emppty(value,"Abstract")
    if len(value) < 100:
        raise ValidationError(
            "This field min 10 max 500",
            code="invalid_title"
        )
    check_not_xss(value,"Abstract")



def validate_keyword(value:list) -> None:
    if not value:
        raise ValidationError(
            "keyword must be been"
        )
    if len(value) < 4 or len(value) > 6:
        raise ValidationError(
            "keyword must be min 4 max 6"
        )

def validate_file(file) -> None:
    max_file_size = 10 * 1024 * 1024
    name = file.name.split(".")[-1].lower()
    if file.size > max_file_size:
        raise ValidationError(
            "Max file upload 10 mb"
        )

    allowed_file_path = ["pdf","docx","doc"]

    if name not in allowed_file_path:
        raise ValidationError(
            "only upload pdf or docx file "
        )


def validate_cover_letter(value:str) -> None:
    if not value:
        return
    check_not_xss(value,"Cover letter")










