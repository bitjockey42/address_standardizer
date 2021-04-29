import csv
import json
import pathlib

from collections import defaultdict

PARENT_DIR = pathlib.Path(__file__).parent.parent.absolute()


def read_csv(filename):
    with open(filename, newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        return [row for row in reader]


def write_json(data, filename):
    with open(filename, "w+") as json_file:
        json.dump(data, json_file, indent=4)


def read_json(filename):
    with open(filename) as json_file:
        return json.load(json_file)


def process_csv(filename):
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


def generate_standards_map(filename):
    rows = process_csv(filename)
    standards_map = defaultdict(list)

    for row in rows:
        standards_map[row["standard"]].append(row["common"])

    return standards_map


def generate_lookup_map(filename):
    rows = process_csv(filename)
    lookup_map = defaultdict(str)

    for row in rows:
        lookup_map[row["common"]] = row["standard"]

    return lookup_map
