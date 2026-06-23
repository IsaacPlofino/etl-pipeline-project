# ETL Pipeline Project — Isaac Plofino

A modular Python ETL pipeline built as part of the IBM DataStage Sprint (June 2026). Demonstrates the Extract, Transform, Load architecture that underpins IBM DataStage pipelines — built from scratch after zero prior Python experience.

**Stack:** Python 3.13 · csv · MySQL 8.4  
**Sprint target:** IBM Consulting Associates — DataStage/Cloud track  
**Companion repo:** [github.com/IsaacPlofino/sql-practice](https://github.com/IsaacPlofino/sql-practice)

---

## Project Structure

```
etl-pipeline-project/
│
├── extract.py           # Reads raw data from source CSV
├── transform.py         # Applies business rules and enriches records
├── load.py              # Routes valid and rejected records to separate outputs
├── pipeline.py          # Orchestrates the full ETL flow
│
├── data/
│   └── orders.csv       # Source data (sprint_db schema)
│
├── output/
│   ├── orders_clean.csv     # Valid records
│   └── orders_rejected.csv  # Rejected records (flagged for review)
│
├── foundations/
│   └── day_B4_etl_basics.py   # Python basics built before the pipeline
│
├── notes/
│   └── day_B3_etl_concepts_notes.md   # ETL theory and IBM DataStage notes
│
└── .gitignore
```

---

## How to Run

```bash
# Clone the repo
git clone https://github.com/IsaacPlofino/etl-pipeline-project.git
cd etl-pipeline-project

# Run the pipeline
python pipeline.py
```

**Expected output:**
```
==================================================
IBM DataStage Sprint — ETL Pipeline
==================================================
[EXTRACT]   4 records read from data/orders.csv
[TRANSFORM] 4 records processed, 3 valid
[LOAD]      3 valid records written to output/orders_clean.csv
[LOAD]      1 rejected records written to output/orders_rejected.csv
==================================================
Pipeline complete.
  Total records  : 4
  Valid records  : 3
  Invalid records: 1
  Total revenue  : 44,700.00
==================================================
```

---

## Pipeline Architecture

Each file has exactly one responsibility — same separation of concerns as a DataStage job canvas.

### extract.py — Source Stage
Reads raw CSV data and returns it as a list of dictionaries. No transformation happens here. Includes error handling for missing source files — returns an empty list instead of crashing the pipeline.

```python
def extract(filepath):
    # Reads source CSV → returns raw records as list of dicts
    # Every value comes in as a string — type conversion happens in transform
    # FileNotFoundError is caught and handled gracefully
```

### transform.py — Transformer Stage
Applies all business rules in one place. Three reusable functions plus the main `transform()` orchestrator:

| Function | What it does | DataStage equivalent |
|----------|-------------|---------------------|
| `calculate_revenue()` | quantity × price | Transformer expression |
| `categorize_revenue()` | Low / Mid / High / Zero | CASE WHEN logic |
| `is_valid_order()` | quantity > 0, status ≠ cancelled | Filter stage condition |
| `transform()` | Type conversion + applies all rules | Full Transformer stage |

**Type conversion is explicit here** — CSV gives everything as strings. Converting before math is mandatory. A missing `int()` or `float()` is a pipeline crash at 2am during a client's batch run.

### load.py — Target Stage
Splits transformed records into two output files based on the `is_valid` flag. Valid records go to `orders_clean.csv`. Rejected records go to `orders_rejected.csv` for review and reprocessing. No business logic lives here — just routing and writing.

```python
def load(records, clean_filepath, rejected_filepath):
    # Splits on is_valid flag using list comprehensions
    # Writes each group to a separate CSV with headers
    # fieldnames controls column order in both outputs
```

### pipeline.py — Job Orchestrator
Calls extract → transform → load in sequence, then prints a run summary. Uses `if __name__ == "__main__"` so the pipeline only runs when executed directly — not when imported by another file.

```python
raw_records         = extract("data/orders.csv")
transformed_records = transform(raw_records)
load(transformed_records, "output/orders_clean.csv", "output/orders_rejected.csv")
```

---

## Data Schema

Source data uses the `sprint_db` schema from the companion SQL repo:

```
orders.csv columns:
  order_id       → int
  customer_name  → str
  quantity       → int   (converted from string on extract)
  price          → float (converted from string on extract)
  status         → str   (stripped and lowercased on transform)
```

**Output adds three enriched columns:**
- `revenue` — quantity × price
- `category` — Zero Revenue / Low / Mid / High
- `is_valid` — True / False (quantity > 0 and status ≠ cancelled)

**Validation rules (applied in transform):**
- `quantity <= 0` → rejected
- `status == "cancelled"` → rejected
- All other records → valid

---

## Foundations

The `/foundations` folder contains `day_B4_etl_basics.py` — the Python learning file built the day before the pipeline. It covers:

- Variables and data types
- Lists and dictionaries
- Loops and conditionals
- Functions with return values
- CSV read/write with `csv.DictReader` and `csv.DictWriter`
- Pandas basics — DataFrame load, filtering, groupby, export

This progression — theory → basics → modular pipeline — mirrors how IBM onboards DataStage Associates.

---

## IBM DataStage Connection

Every component of this pipeline maps directly to a DataStage stage:

| This pipeline | DataStage equivalent |
|--------------|---------------------|
| `extract.py` | Sequential File stage (source) |
| `transform.py` | Transformer stage |
| `is_valid_order()` | Filter stage |
| `calculate_revenue()` | Transformer expression |
| `categorize_revenue()` | CASE WHEN in Transformer |
| `load.py` — valid path | Sequential File stage (target) |
| `load.py` — rejected path | Reject link / error output |
| `pipeline.py` | DataStage job orchestrator |

The tool changes depending on the client environment. The thinking doesn't.

---

## Profile

**Degree:** BSIT-Business Analytics, Cum Laude — Bulacan State University SJDM  
**Awards:** Gold Gear Award (Dean's List all 4 years)  
**Target:** IBM Consulting Associates — DataStage/Cloud track  
**SQL repo:** [github.com/IsaacPlofino/sql-practice](https://github.com/IsaacPlofino/sql-practice)
