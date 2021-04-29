import csv


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
