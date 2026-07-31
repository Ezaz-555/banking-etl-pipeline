# Financial Data Platform

A Python-based ETL (Extract, Transform, Load) project that simulates a banking system by generating synthetic financial data, cleaning it, and loading it into a PostgreSQL database.

This project demonstrates fundamental Data Engineering concepts, including data ingestion, transformation, loading, and validation using a modular Python architecture.

---

## Project Overview

The project simulates a financial institution by generating synthetic datasets for:

- Customers
- Accounts
- Branches
- Cards
- Loans
- Transactions

The generated CSV files are processed through an ETL pipeline and loaded into PostgreSQL.

---

## Features

- Generate realistic banking datasets
- Modular ETL pipeline
- Data validation by removing duplicate records
- Load data into PostgreSQL using SQLAlchemy
- Database validation through SQL queries
- Clean and maintainable project structure

---

## Tech Stack

- Python 3.x
- Pandas
- PostgreSQL
- SQLAlchemy
- Psycopg2
- python-dotenv

---

## Project Structure

```text
financial-data-platform/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│
├── src/
│   ├── analytics/
│   │   └── data_summary.py
│   │
│   ├── generators/
│   │
│   ├── ingestion/
│   │   └── csv_reader.py
│   │
│   ├── transformation/
│   │   └── data_cleaner.py
│   │
│   ├── loading/
│   │   └── load_to_postgres.py
│   │
│   └── utils/
│       ├── config.py
│       └── database.py
│
├── main.py
├── requirements.txt
├── README.md
└── .env
```

---

## ETL Workflow

```text
Generate Data
      │
      ▼
CSV Files
      │
      ▼
Ingestion
(Read CSV)
      │
      ▼
Transformation
(Remove Duplicates)
      │
      ▼
Loading
(PostgreSQL)
      │
      ▼
Validation
(Row Count Verification)
```

---

## Database Tables

| Table | Description |
|--------|-------------|
| customers | Customer information |
| accounts | Bank account details |
| branches | Branch information |
| cards | Debit/Credit card details |
| loans | Loan information |
| transactions | Financial transactions |

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Ezaz-555/banking-etl-pipeline.git
cd banking-etl-pipeline
```

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate the environment.

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file.

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=financial_db
DB_USER=postgres
DB_PASSWORD=*****
```

### 5. Run the ETL Pipeline

```bash
python main.py
```

### 6. Validate Loaded Data

```bash
python src/analytics/data_summary.py
```

---

## Sample Output

```text
========== DATABASE SUMMARY ==========

Customers      : 1000
Accounts       : 1500
Branches       : 20
Cards          : 1200
Loans          : 300
Transactions   : 5000

======================================
```

---

## Key Learnings

- Python ETL pipeline development
- Data cleaning using Pandas
- PostgreSQL integration with SQLAlchemy
- Modular project architecture
- SQL-based data validation
- Environment variable management using python-dotenv

---

## Future Enhancements

- Store raw CSV files in Amazon S3
- Use Amazon RDS for PostgreSQL
- Deploy ETL pipeline on Amazon EC2
- Schedule ETL execution using Apache Airflow

---

## Author

**Ezaz Ahmed Mohammad**

- GitHub: https://github.com/Ezaz-555
- LinkedIn: https://www.linkedin.com/in/ezaz-ahmed-mohammad-8430571b4
