# Etl Sales Pipeline Postgres
ETL pipeline that extracts CSV sales data, validates and cleans it, and loads it into PostgreSQL using Python.

Tech Stack:
- Python (pandas)
- PostgreSQL
- Docker
- logging

Functionality:
1. Extract: CSV / mock data
2. Transform:
- schema validation
- missing values
- type casting
3. Load:
- staging → final tables
- basic data quality checks
