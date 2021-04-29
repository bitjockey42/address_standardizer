"""Main module."""
import re

from address_standardizer.abbreviator import abbreviate


def standardize(address):
    def standardize_part(part):
        if abbreviate(part) is None:
            return part
        else:
            return abbreviate(part)

    parts = split_parts(address)

    return " ".join(list(map(standardize_part, parts)))


def split_parts(string):
    parts = string.upper().strip().split(" ")
    return list(map(sanitize, parts))


def sanitize(string):
    return re.sub(r"[^a-zA-Z0-9]+", "", string.upper())
