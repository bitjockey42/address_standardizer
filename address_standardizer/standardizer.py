"""Main module."""
from address_standardizer.abbreviator import abbreviate


def standardize(address):
    parts = address.upper().strip().split(" ")

    for i, part in enumerate(parts):
        if abbreviate(part) is None:
            continue

        parts[i] = abbreviate(part)

    return " ".join(parts)
