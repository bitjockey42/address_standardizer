"""Get abbreviations"""
from address_standardizer.constants import (
    LOOKUP_C1,
    LOOKUP_C2,
    LOOKUP_DIRECTIONAL,
    LOOKUP_STATES,
    LOOKUP_BUSINESS,
)


def abbreviate(string: str) -> str:
    if not string:
        return None

    lookup_value = string.upper()

    return (
        LOOKUP_C1.get(lookup_value)
        or LOOKUP_C2.get(lookup_value)
        # or LOOKUP_STATES.get(lookup_value)
        or LOOKUP_DIRECTIONAL.get(lookup_value)
        # or LOOKUP_BUSINESS.get(lookup_value)
    )


def abbreviate_state(string: str) -> str:
    if not string:
        return None

    lookup_value = string.upper()

    return LOOKUP_STATES.get(lookup_value)


def abbreviate_business(string: str) -> str:
    if not string:
        return None

    lookup_value = string.upper()

    return LOOKUP_BUSINESS.get(lookup_value)
