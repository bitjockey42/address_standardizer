"""Get abbreviations"""
from address_standardizer.utils import read_json, PARENT_DIR

LOOKUP_C1 = read_json(str(PARENT_DIR.joinpath("data", "lookup_map_c1.json")))


def abbreviate(suffix):
    return LOOKUP_C1.get(suffix.upper())
