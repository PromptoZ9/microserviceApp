import string

param1 = string.ascii_letters
param2 = string.digits
param3 = string.punctuation
param4 = string.ascii_lowercase
param5 = string.ascii_uppercase
password = "12bcd|345a"

def check_password(password : str, param : str):
    for p in password:
        if p in param:
            return True

    return False
print(check_password(password, param5))
exit()


import re

def has_ascii_letter(s):
    return bool(re.search(r"^[^a-zA-Z]*[a-sA-Z][^a-zA-Z]*|^[a-zA-Z]+$", s))

def has_digit(s):
    return bool(re.search(r".*\d.*", s))

def has_punctuation(s):
    return bool(re.search(r".*[!@#$%^&|*()_\-+=\{\}:;\"'<>,./?].*", s))

print(has_ascii_letter(password))
print(has_digit(password))
print(has_punctuation(password))



