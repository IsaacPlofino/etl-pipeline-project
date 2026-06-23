# load.py
# Responsibility: write transformed records to output CSVs
# Valid records → orders_clean.csv
# Invalid records → orders_rejected.csv

import csv

def load(records, clean_filepath, rejected_filepath):
    fieldnames = [
        "order_id",
        "customer_name",
        "quantity",
        "price",
        "status",
        "revenue",
        "category",
        "is_valid"
    ]

    # Split records into two lists based on is_valid flag
    valid_records    = [r for r in records if r["is_valid"]]
    rejected_records = [r for r in records if not r["is_valid"]]

    # Write valid records
    with open(clean_filepath, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(valid_records)

    print(f"[LOAD] {len(valid_records)} valid records written to {clean_filepath}")

    # Write rejected records
    with open(rejected_filepath, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rejected_records)

    print(f"[LOAD] {len(rejected_records)} rejected records written to {rejected_filepath}")