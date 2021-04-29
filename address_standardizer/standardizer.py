"""Main module."""
import re

from address_standardizer.abbreviator import abbreviate


def standardize(address):
    def _standardize(part):
        if abbreviate(part) is None:
            return part
        else:
            return abbreviate(part)

    parts = split_parts(address)

    return " ".join(list(map(_standardize, parts)))


def split_parts(string):
    parts = string.upper().strip().split(" ")
    return list(map(sanitize, parts))


def sanitize(string):
    return re.sub(r"[^a-zA-Z0-9]+", "", string.upper())
