# ETL Design

## Overview

The Financial Data Platform follows an ETL (Extract, Transform, Load) process to move banking data from raw CSV files into a PostgreSQL database.

The pipeline is implemented in Python and uses Pandas for data processing and SQLAlchemy for database connectivity.

---

# ETL Workflow

```text
          Raw CSV Files
                │
                ▼
          Data Extraction
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
          ETL Summary
                │
                ▼
           SQL Analytics