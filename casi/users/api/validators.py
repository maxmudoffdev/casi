from casi.common.func import chek_not_none_or_emppty,check_short,check_not_xss,check_number_or_letter


def validate_first_name(value:str) -> None:
    chek_not_none_or_emppty(value,"First name")
    check_short(value,"First name")
    check_not_xss(value,"First name")


def validate_last_name(value:str) -> None:
    chek_not_none_or_emppty(value,"Last name")
    check_short(value,"last name")
    check_not_xss(value,"Last name")


def validate_email(value:str) -> None:
    chek_not_none_or_emppty(value, "Email")
    check_not_xss(value, "Email")



