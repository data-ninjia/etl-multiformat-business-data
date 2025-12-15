# Multi-format Business ETL Pipeline

## Overview
This project implements a production-like ETL pipeline that processes
business data from multiple source formats (CSV, JSON, XML, Parquet)
and loads normalized data into PostgreSQL.

## Business Context
The pipeline simulates an e-commerce analytics system where data
comes from different upstream systems and file formats.

## Data Sources
- Orders: CSV
- Customers: JSON
- Suppliers: XML
- Events: Parquet

## Architecture
Source Files → Extract → Transform → Validation → Staging → Core Tables

## Tech Stack
- Python (pandas, pyarrow)
- PostgreSQL
- Docker / Docker Compose

## Data Quality Checks
- Schema validation
- Null checks
- Referential integrity
- Duplicate detection

## How to Run
```bash
docker-compose up --build
