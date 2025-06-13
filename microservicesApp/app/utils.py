import re

def has_ascii_letter(s):
    return bool(re.search(r"^[^a-zA-Z]*[a-sA-Z][^a-zA-Z]*|^[a-zA-Z]+$", s))

def has_digit(s):
    return bool(re.search(r".*\d.*", s))

def has_punctuation(s):
    return bool(re.search(r".*[!@#$%^&|*()_\-+=\{\}:;\"'<>,./?].*", s))

def uplowcase_password(password : str, param : str):
    for p in password:
        if p in param:
            return True

    return False