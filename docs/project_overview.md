# Financial Data Platform

## Project Overview

The Financial Data Platform is an end-to-end Data Engineering project that simulates a banking data processing environment.

The project generates synthetic banking datasets representing customers, accounts, branches, cards, loans, and transactions. These datasets are processed through a Python-based ETL pipeline and loaded into a PostgreSQL database for SQL-based analysis.

The project demonstrates practical Data Engineering concepts including data ingestion, data cleaning, validation, database loading, upsert handling, logging, error handling, and analytical querying.

---

# Business Problem

Banking systems typically contain multiple types of data related to customers, accounts, transactions, loans, cards, and branches.

For analytical purposes, these datasets need to be collected, processed, validated, and stored in a structured format.

This project simulates that process by:

- Generating synthetic banking datasets.
- Processing the datasets through an ETL pipeline.
- Validating required fields.
- Removing duplicate records.
- Loading the processed data into PostgreSQL.
- Using SQL queries to analyze the resulting data.

The platform can be used to answer questions such as:

- Which customers have the highest transaction activity?
- Which accounts have the highest balances?
- What is the total transaction amount by transaction type?
- Which loan types are most common?
- How are accounts distributed across branches?

---

# Project Objectives

The primary objectives of this project are:

- Build an end-to-end batch ETL pipeline using Python.
- Process multiple related banking datasets.
- Perform basic data cleaning and validation.
- Design a relational PostgreSQL database.
- Load data using PostgreSQL upsert logic.
- Implement logging and dataset-level error handling.
- Execute SQL-based analytical queries.
- Demonstrate practical Data Engineering concepts using a modular project structure.

---

# Project Scope

The project currently covers:

- Customer data
- Account data
- Branch data
- Card data
- Loan data
- Transaction data
- CSV data ingestion
- Duplicate removal
- Required-field validation
- PostgreSQL loading
- PostgreSQL upserts
- ETL logging
- Error handling
- SQL analytics

The project currently does not include:

- Real-time streaming
- Internet banking functionality
- User authentication
- Payment gateway integration
- Mobile applications
- Production cloud deployment
- Workflow orchestration

---

# Dataset Overview

The project currently processes six synthetic datasets:

| Dataset | Approximate Records |
|---------|---------------------:|
| Customers | 1,000 |
| Accounts | 1,500 |
| Branches | 20 |
| Cards | 1,200 |
| Loans | 300 |
| Transactions | 5,000 |

Total records processed: approximately **9,020**.

---

# Technology Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| Data Processing | Pandas |
| Database | PostgreSQL |
| Database Connectivity | SQLAlchemy |
| PostgreSQL Driver | psycopg2 |
| Configuration Management | python-dotenv |
| Data Generation | Faker |
| Version Control | Git |
| Repository | GitHub |
| Development Environment | PyCharm |

### Cloud Technologies

Cloud technologies are not part of the current implementation.

Potential cloud components such as Amazon S3 and AWS-based data services may be introduced as future enhancements.

---

# High-Level Architecture

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
                  ETL Execution Log
                         │
                         ▼
                  ETL Summary
                         │
                         ▼
                   SQL Analytics