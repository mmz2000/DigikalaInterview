import functools
import re

from settings import ASSETS_DIR


def has_numbers(input_string):
    return bool(re.search(r"\d", input_string))


def has_upper(input_string):
    return bool(re.search(r"[A-Z]", input_string))


def has_lower(input_string):
    return bool(re.search(r"[a-z]", input_string))


def has_special(input_string):
    return bool(re.search(r"[^A-Za-z0-9]", input_string))


@functools.cache
def load_common_passwords():
    common_password_path = ASSETS_DIR / "common_password.txt"
    return common_password_path.read_text().splitlines()


@functools.cache
def is_not_common(input_string):
    return input_string not in load_common_passwords()


def validate_password(password: str) -> bool:
    return (
        len(password) >= 8
        and is_not_common(password)
        and has_lower(password)
        and has_upper(password)
        and has_numbers(password)
        and has_special(password)
    )
