# Data Dictionary

## Overview

The data dictionary defines the structure, meaning, and data type of every column used in the Financial Data Platform. It serves as a reference for developers, data engineers, analysts, and business users.

---

# Customers Table

| Column | Data Type | Nullable | Description | Example |
|---------|-----------|----------|-------------|---------|
| customer_id | INT | No | Unique customer identifier | 1001 |
| first_name | VARCHAR(50) | No | Customer first name | Rahul |
| last_name | VARCHAR(50) | No | Customer last name | Sharma |
| date_of_birth | DATE | No | Customer's date of birth | 1995-08-14 |
| gender | VARCHAR(10) | Yes | Customer gender | Male |
| city | VARCHAR(100) | No | Customer city | Bangalore |
| occupation | VARCHAR(100) | Yes | Customer occupation | Software Engineer |
| annual_income | DECIMAL(12,2) | Yes | Annual income | 1200000.00 |

---

# Accounts Table

| Column | Data Type | Nullable | Description | Example |
|---------|-----------|----------|-------------|---------|
| account_id | INT | No | Unique account identifier | 5001 |
| customer_id | INT | No | Customer reference | 1001 |
| branch_id | INT | No | Branch reference | 201 |
| account_type | VARCHAR(20) | No | Type of account | Savings |
| balance | DECIMAL(12,2) | No | Current account balance | 25000.50 |
| open_date | DATE | No | Account opening date | 2023-01-15 |
| status | VARCHAR(20) | No | Account status | Active |

---

# Transactions Table

| Column | Data Type | Nullable | Description | Example |
|---------|-----------|----------|-------------|---------|
| transaction_id | INT | No | Unique transaction identifier | 900001 |
| account_id | INT | No | Account reference | 5001 |
| transaction_date | TIMESTAMP | No | Date and time of transaction | 2026-07-29 10:15:30 |
| transaction_type | VARCHAR(20) | No | Credit or Debit | Debit |
| amount | DECIMAL(12,2) | No | Transaction amount | 1500.00 |
| channel | VARCHAR(30) | Yes | Transaction channel | UPI |
| status | VARCHAR(20) | No | Transaction status | Success |

---

# Loans Table

| Column | Data Type | Nullable | Description | Example |
|---------|-----------|----------|-------------|---------|
| loan_id | INT | No | Unique loan identifier | 7001 |
| customer_id | INT | No | Customer reference | 1001 |
| loan_type | VARCHAR(30) | No | Type of loan | Home Loan |
| loan_amount | DECIMAL(12,2) | No | Total loan amount | 2500000.00 |
| interest_rate | DECIMAL(5,2) | No | Annual interest rate | 8.50 |
| loan_status | VARCHAR(20) | No | Loan status | Active |

---

# Cards Table

| Column | Data Type | Nullable | Description | Example |
|---------|-----------|----------|-------------|---------|
| card_id | INT | No | Unique card identifier | 3001 |
| customer_id | INT | No | Customer reference | 1001 |
| card_type | VARCHAR(20) | No | Debit or Credit | Debit |
| card_network | VARCHAR(20) | No | Card network | Visa |
| expiry_date | DATE | No | Card expiry date | 2029-05-31 |
| card_status | VARCHAR(20) | No | Card status | Active |

---

# Branches Table

| Column | Data Type | Nullable | Description | Example |
|---------|-----------|----------|-------------|---------|
| branch_id | INT | No | Unique branch identifier | 201 |
| branch_name | VARCHAR(100) | No | Branch name | Electronic City Branch |
| city | VARCHAR(100) | No | Branch city | Bangalore |
| state | VARCHAR(100) | No | Branch state | Karnataka |
| manager_name | VARCHAR(100) | Yes | Branch manager | Amit Kumar |

---

# Notes

- Primary keys uniquely identify each record.
- Foreign keys establish relationships between tables.
- `DECIMAL` is used for monetary values to maintain precision.
- `DATE` stores calendar dates, while `TIMESTAMP` stores both date and time.
- Nullable fields are optional and may contain missing values.