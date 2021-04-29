import csv
import json
import pathlib

from typing import List, Dict
from collections import defaultdict

PARENT_DIR = pathlib.Path(__file__).parent.parent.absolute()
DATA_DIR = PARENT_DIR.joinpath("data")


def read_csv(filename: str) -> List[Dict]:
    with open(filename, newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        return [row for row in reader]


def write_json(data: Dict, filename: str):
    with open(filename, "w+") as json_file:
        json.dump(data, json_file, indent=4)


def read_json(filename: str) -> Dict:
    with open(filename) as json_file:
        return json.load(json_file)


def process_csv(filename: str) -> List[Dict]:
    rows = read_csv(filename)

    primary = ""
    standard = ""

    for row in rows:
        primary = row["primary"].upper() if row.get("primary") else primary
        standard = row["standard"].upper() if row.get("standard") else standard

        if primary:
            row["primary"] = primary

        if standard:
            row["standard"] = standard

        row["common"] = row["common"].upper()

    return rows


def process_csv_alt(filename: str) -> List[Dict]:
    """Process CSV where common representations are in one row"""
    rows = read_csv(filename)
    processed = []

    for row in rows:
        commons = row["common"].split("\n ")
        standard = row["standard"]

        for common in commons:
            processed.append({"common": common, "standard": standard})

    return processed


def generate_standards_map(filename: str) -> Dict:
    rows = process_csv(filename)
    standards_map = defaultdict(list)

    for row in rows:
        standards_map[row["standard"]].append(row["common"])

    return standards_map


def generate_lookup_map(processed_rows: List[Dict]) -> Dict:
    lookup_map = defaultdict(str)

    for row in processed_rows:
        lookup_map[row["common"]] = row["standard"]

    return lookup_map
