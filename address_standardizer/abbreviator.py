"""Get abbreviations"""
from address_standardizer.utils import read_json, DATA_DIR

LOOKUP_C1 = read_json(str(DATA_DIR.joinpath("lookup_map_c1.json")))
LOOKUP_C2 = read_json(str(DATA_DIR.joinpath("lookup_map_c2.json")))
LOOKUP_STATES = read_json(str(DATA_DIR.joinpath("lookup_map_states.json")))
LOOKUP_DIRECTIONAL = read_json(str(DATA_DIR.joinpath("lookup_map_directional.json")))


def abbreviate(string: str) -> str:
    if not string:
        raise ValueError("String cannot be empty")

    lookup_value = string.upper()

    return (
        LOOKUP_C1.get(lookup_value)
        or LOOKUP_C2.get(lookup_value)
        or LOOKUP_STATES.get(lookup_value)
        or LOOKUP_DIRECTIONAL.get(lookup_value)
    )
