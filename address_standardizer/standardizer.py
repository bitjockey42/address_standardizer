"""Main module."""
import re

from typing import List

from address_standardizer.abbreviator import abbreviate, abbreviate_business


def standardize(address: str) -> str:
    """Standardize address"""
    if not address:
        return ""

    def standardize_part(part):
        if abbreviate(part) is None:
            return part
        else:
            return abbreviate(part)

    parts = split_parts(address)

    return " ".join(list(map(standardize_part, parts)))


def standardize_business(business: str) -> str:
    """Standardize business"""
    if not business:
        return ""

    def standardize_part(part):
        if abbreviate_business(part) is None:
            return part
        else:
            return abbreviate_business(part)

    parts = split_parts(business)

    return " ".join(list(map(standardize_part, parts)))


def split_parts(string: str) -> List[str]:
    """Split address into parts"""
    parts = string.upper().strip().split(" ")
    return list(map(sanitize, parts))


def sanitize(string: str) -> str:
    """Remove special characters"""
    return re.sub(r"[^a-zA-Z0-9\/]+", "", string.upper())
