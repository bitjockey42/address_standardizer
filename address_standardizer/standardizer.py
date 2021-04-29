"""Main module."""
import re

from typing import List

from address_standardizer.abbreviator import abbreviate


def standardize(address: str) -> str:
    """Standardize address"""
    if not address:
        return None

    def standardize_part(part):
        if abbreviate(part) is None:
            return part
        else:
            return abbreviate(part)

    parts = split_parts(address)

    return " ".join(list(map(standardize_part, parts)))


def split_parts(string: str) -> List[str]:
    """Split address into parts"""
    parts = string.upper().strip().split(" ")
    return list(map(sanitize, parts))


def sanitize(string: str) -> str:
    """Remove special characters"""
    return re.sub(r"[^a-zA-Z0-9]+", "", string.upper())
