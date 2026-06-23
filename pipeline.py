#pipeline.py
#Responsibility: orchestrate the full ETL pipeline. Extract, Transform, Load

from extract import extract
from transform import transform
from load import load

def run_pipeline():
    print("=" * 50)
    print("IBM DataStage Sprint — ETL Pipeline")
    print("=" * 50)
    
    #Step 1 Extract
    raw_records = extract("data/orders.csv")
    
    #Step 2 Transform
    transformed_records = transform(raw_records)
    
    # Step 3: Load
    load(
        transformed_records,
        "output/orders_clean.csv",
        "output/orders_rejected.csv"
    )
    
    #Summary
    total    = len(transformed_records)
    valid    = sum(1 for r in transformed_records if r["is_valid"])
    invalid = total - valid
    revenue  = sum(r["revenue"] for r in transformed_records)
    
    print("=" * 50)
    print(f"Pipeline complete.")
    print(f"  Total records  : {total}")
    print(f"  Valid records  : {valid}")
    print(f"  Invalid records: {invalid}")
    print(f"  Total revenue  : {revenue:,.2f}")
    
    
if __name__=="__main__":
    run_pipeline()