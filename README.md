# ETL Pipeline Project — Isaac Plofino

A modular Python ETL pipeline built as part of the IBM DataStage Sprint. This project demonstrates the core Extract, Transform, Load (ETL) architecture that underpins enterprise data integration tools like IBM DataStage—built from scratch to showcase rapid upskilling and architectural adaptability.Stack: Python 3.13 · pandas · csv · MySQL 8.4Sprint Target: IBM Consulting Associates — DataStage/Cloud TrackCompanion Repo: github.com/IsaacPlofino/sql-practice📂 Project StructurePlaintextetl-pipeline-project/
│
├── extract.py                # Reads raw data from source CSV
├── transform.py              # Applies business rules and enriches records
├── load.py                   # Writes clean data to target destination
├── pipeline.py               # Orchestrates the full ETL workflow
│
├── data/
│   └── orders.csv            # Source data (sprint_db schema)
│
├── foundations/
│   └── day_B4_etl_basics.py  # Python and Pandas fundamentals core exercises
│
├── notes/
│   └── day_B3_etl_concepts_notes.md  # ETL theory and IBM DataStage deep-dive notes
│
└── .gitignore
🚀 How to RunBash# Clone the repository
git clone https://github.com/IsaacPlofino/etl-pipeline-project.git
cd etl-pipeline-project

# Execute the pipeline orchestrator
python pipeline.py
Expected Runtime Output:Plaintext==================================================
IBM DataStage Sprint — ETL Pipeline
==================================================
[EXTRACT]   4 records read from data/orders.csv
[TRANSFORM] 4 records processed, 3 valid
[LOAD]      4 records written to output/orders_clean.csv
==================================================
Pipeline complete.
  Total records  : 4
  Valid records  : 3
  Invalid records: 1
  Total revenue  : 44,700.00
==================================================
🏗️ Pipeline ArchitectureEach script is decoupled and handles exactly one responsibility—mirroring the strict separation of concerns found on an IBM DataStage job canvas.🔌 extract.py — Source StageExtracts raw data from flat files and parses them into memory.Design: Decoupled by accepting the filepath as an argument, allowing the pipeline to target different source environments without code modifications.Note: Values are treated as strings upon extraction; data sanitization and type casting are deferred to the transformation stage.⚙️ transform.py — Transformer StageActs as the central execution engine for business logic and data cleaning. It handles explicit type casting and features three specialized helper operations:FunctionOperational LogicDataStage Equivalentcalculate_revenue()quantity × priceTransformer Expressioncategorize_revenue()Buckets revenue (Low / Mid / High / Zero)CASE WHEN Conditional Logicis_valid_order()Filters out invalid quantities or cancelled ordersFilter Stage Conditiontransform()Orchestrated data cleaning & enrichmentFull Transformer Stage⚠️ Data Integrity Note: Because CSV values default to strings, explicit casting via int() and float() is enforced. Ensuring structural type safety here prevents downstream pipeline failures during automated production batches.📥 load.py — Target StagePersists transformed data into its final destination.Design: Contains no business logic. It handles layout mappings (fieldnames formatting) so that changing downstream environments (e.g., from CSV to a relational MySQL target) requires modifying only this module.🎮 pipeline.py — Job OrchestratorThe main driver that chains extract $\rightarrow$ transform $\rightarrow$ load in a functional pipeline.Uses a Python procedural guard (if __name__ == "__main__":) ensuring the script only runs when executed directly, preventing accidental pipeline execution when components are imported by other modules.📊 Data SchemaThe pipeline consumes the sprint_db schema from the companion SQL repository:PlaintextSource Schema (orders.csv):
  ├── order_id       → int
  ├── customer_name  → str
  ├── quantity       → int   (Cast from string during transform)
  ├── price          → float (Cast from string during transform)
  └── status         → str   (Normalized to lowercase during transform)
Enriched Output Fields:revenue: Calculated financial value ($quantity \times price$).category: Performance tier classifications (Zero Revenue / Low / Mid / High).is_valid: Boolean flag checking if data passes business health checks ($quantity > 0$ and $status \neq \text{'cancelled'}$).📈 FoundationsThe /foundations directory tracks my rapid progression from functional syntax to pipeline assembly via day_B4_etl_basics.py. Key concepts mastered include:Primitive types, nested lists, and key-value dictionaries.Control flow logic, iterable loops, and structured error handling.File I/O operations using native csv.DictReader and csv.DictWriter.Data manipulation with Pandas (DataFrames, conditional slicing, groupby aggregations, and performance writes).This structural learning path directly mirrors the production onboarding framework used for incoming enterprise Data Engineers.🤝 IBM DataStage Paradigm MappingThe logic driving this script is designed to translate natively into corporate DataStage job flows:Python ComponentDataStage Stage Equivalentextract.pySequential File Stage (Source)transform.pyTransformer Stageis_valid_order()Filter Stagecalculate_revenue()Transformer Inline Expressioncategorize_revenue()Derivation Constraints / CASE Logicload.pySequential File / DB Design Connector (Target)pipeline.pyDataStage Director / Sequence Job Orchestration👤 ProfileDegree: BSIT-Business Analytics, Cum Laude — Bulacan State University SJDMAwards: Gold Gear Award (Dean's List all 4 academic years)Target Role: IBM Consulting Associates — DataStage/Cloud TrackSQL Repository: github.com/IsaacPlofino/sql-practice
