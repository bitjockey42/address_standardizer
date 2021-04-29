"""Get abbreviations"""
from address_standardizer.utils import read_json, DATA_DIR

LOOKUP_C1 = read_json(str(DATA_DIR.joinpath("lookup_map_c1.json")))
LOOKUP_C2 = read_json(str(DATA_DIR.joinpath("lookup_map_c2.json")))


def abbreviate(suffix):
    return LOOKUP_C1.get(suffix.upper()) or LOOKUP_C2.get(suffix.upper())
