# Financial Data Platform

A Python-based ETL pipeline that simulates a banking data platform by generating synthetic financial datasets, processing and validating the data, and loading it into PostgreSQL for SQL-based analysis.

The project demonstrates practical Data Engineering concepts including data ingestion, data cleaning, validation, PostgreSQL upserts, logging, error handling, and analytical querying.

---

## Project Overview

The platform simulates a banking environment with six related datasets:

- Customers
- Accounts
- Branches
- Cards
- Loans
- Transactions

The datasets are generated as CSV files and processed through a Python ETL pipeline before being loaded into PostgreSQL.

The current project processes approximately **9,020 records** across the six datasets.

---

## ETL Pipeline

```text
Synthetic CSV Files
        │
        ▼
   Data Ingestion
        │
        ▼
 Duplicate Removal
        │
        ▼
Required Field Validation
        │
        ▼
 PostgreSQL Upsert
        │
        ▼
 Logging & Error Handling
        │
        ▼
  ETL Execution Summary
        │
        ▼
    SQL Analytics