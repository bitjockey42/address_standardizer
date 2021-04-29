import csv

from collections import defaultdict


def read_csv(filename):
    with open(filename, newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        return [row for row in reader]


def process_csv(filename):
    rows = read_csv(filename)

    for row in rows:
        if row["primary"] and row["standard"]:
            primary = row["primary"]
            standard = row["standard"]

        if not row["primary"] and not row["standard"]:
            row["primary"] = primary
            row["standard"] = standard

    return rows


def generate_standards_map(filename):
    rows = process_csv(filename)
    standards_map = defaultdict(list)

    for row in rows:
        standards_map[row["standard"]].append(row["common"])

    return standards_map
