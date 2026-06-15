#transform.py
#Responsibility: clean, validate, and enrich raw records

def calculate_revenue(quantity, price):
    return quantity * price

def categorize_revenue(revenue):
    if revenue == 0:
        return "Zero Revenue"
    elif revenue < 2000:
        return "Low"
    elif revenue <= 10000:
        return "Mid"
    else:
        return "High"
    
def is_valid_order(order):
    if order["quantity"] <= 0:
        return False
    if order["status"] == "cancelled":
        return False
    return True

def transform(raw_records):
    transformed = []
    
    for record in raw_records:
        #Type conversion
        order_id = int(record["order_id"])
        quantity = int(record["quantity"])
        price    = float(record["price"])
        status   = record["status"].strip().lower()
        customer = record["customer_name"].strip()
        
        #Apply business rules
        revenue  = calculate_revenue(quantity, price)
        category = categorize_revenue(revenue)
        valid    = is_valid_order({"quantity": quantity, "status": status})
        
        # Build enriched record
        transformed.append({
            "order_id":      order_id,
            "customer_name": customer,
            "quantity":      quantity,
            "price":         price,
            "status":        status,
            "revenue":       revenue,
            "category":      category,
            "is_valid":      valid
        })
        
    valid_count = sum(1 for r in transformed if r["is_valid"])
    print(f"[TRANSFORM] {len(transformed)} records processed, {valid_count} valid")
    return transformed