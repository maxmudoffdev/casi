import re
from django.core.exceptions import ValidationError
from casi.authors.validators.func import check_not_xss, chek_not_none_or_emppty, check_short, check_number_or_letter


def valideate_firstname(value:str) -> None:
    chek_not_none_or_emppty(value,"Firstname")
    check_short(value,"Firstname")
    check_not_xss(value,"Firstname")
    check_number_or_letter(value,"Firstname")


def valideate_lastname(value:str) -> None:
    chek_not_none_or_emppty(value,"Lastname")
    check_short(value,"Lastname")
    check_not_xss(value,"Lastname")
    check_number_or_letter(value,"Lastname")



def validate_affilation(value: str) -> None:
    chek_not_none_or_emppty(value, "Affliation")
    check_short(value, "Affliation")
    check_not_xss(value, "Affliation")
    check_number_or_letter(value,"Affliation")



def validate_orcid(value:str) -> None:
    if not value:
        return
    pattern = r"^\d{4}-\d{4}-\d{4}-\d{3}[\dX]$"
    if not re.match(pattern,value):
        raise ValidationError(
            "Invalid ORCID format. Correct format: 0000-0002-1825-0097",
            code="invalid_orcid"
        )
    _validate_orcid_checksum(value)

def _validate_orcid_checksum(value:str) -> None:
    orc_id = value.replace("-","")
    total = 0
    for char in orc_id[:-1]:
        total = (total + int(char)) * 2

    remainder = total % 11
    result = (12 - remainder) % 11
    check = "X" if result == 10 else str(result)
    if check != orc_id[-1]:
        raise ValidationError(
            "Invalid ORCID identifier (checksum mismatch).",
            code="invalid_orcid_checksum"
        )


