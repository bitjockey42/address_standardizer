import csv
import json

from collections import defaultdict


def read_csv(filename):
    with open(filename, newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        return [row for row in reader]


def write_json(data, filename):
    with open(filename, "w+") as json_file:
        json.dump(data, json_file, indent=4)


def process_csv(filename):
    rows = read_csv(filename)

    primary = None
    standard = None

    for row in rows:
        if "primary" in row and row.get("primary"):
            primary = row["primary"]

        if "standard" in row and row.get("standard"):
            standard = row["standard"]

        if "primary" in row:
            row["primary"] = primary

        if "standard" in row:
            row["standard"] = standard

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
