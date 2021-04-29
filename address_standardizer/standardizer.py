"""Main module."""
import re

from address_standardizer.abbreviator import abbreviate


def standardize(address):
    parts = address.upper().strip().split(" ")

    for i, part in enumerate(parts):
        # Remove special characters
        part = re.sub(r"[^a-zA-Z0-9]+", "", part)

        if abbreviate(part) is None:
            continue

        parts[i] = abbreviate(part)

    return " ".join(parts)
