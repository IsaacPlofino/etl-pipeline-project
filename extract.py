#extract.py
#Resposibility: read raw data from the source CSV and return it as-is
import csv

def extract(filepath):
    raw_records = []
    
    with open(filepath, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            raw_records.append(row)
            
    print(f"[EXTRACT] {len(raw_records)} records read from {filepath}")
    return raw_records