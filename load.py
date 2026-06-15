#load.py
#Responsibility: write transformed records to the output CSV

import csv

def load(records,filepath):
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
    
    with open(filepath, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)
        
    print(f"[LOAD] {len(records)} records written to {filepath}")
    
    
    