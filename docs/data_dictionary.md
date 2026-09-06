# Data Dictionary

## Overview

The data dictionary defines the structure, meaning, and data type of every column used in the Financial Data Platform.

It serves as a reference for developers, data engineers, and analysts working with the banking datasets.

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
| annual_income | DECIMAL(12,2) | Yes | Customer annual income | 1200000.00 |

---

# Accounts Table

| Column | Data Type | Nullable | Description | Example |
|---------|-----------|----------|-------------|---------|
| account_id | INT | No | Unique account identifier | 5001 |
| customer_id | INT | No | Reference to the customer who owns the account | 1001 |
| branch_id | INT | No | Reference to the branch associated with the account | 201 |
| account_type | VARCHAR(20) | No | Type of bank account | Savings |
| balance | DECIMAL(12,2) | No | Current account balance | 25000.50 |

---

# Branches Table

| Column | Data Type | Nullable | Description | Example |
|---------|-----------|----------|-------------|---------|
| branch_id | INT | No | Unique branch identifier | 201 |
| branch_name | VARCHAR(100) | No | Name of the bank branch | Electronic City Branch |
| city | VARCHAR(100) | No | Branch city | Bangalore |
| state | VARCHAR(100) | No | Branch state | Karnataka |
| manager_name | VARCHAR(100) | Yes | Name of the branch manager | Amit Kumar |

---

# Cards Table

| Column | Data Type | Nullable | Description | Example |
|---------|-----------|----------|-------------|---------|
| card_id | INT | No | Unique card identifier | 3001 |
| customer_id | INT | No | Reference to the customer who owns the card | 1001 |
| card_type | VARCHAR(20) | No | Type of card | Debit |
| expiry_year | INT | No | Year in which the card expires | 2029 |
| card_status | VARCHAR(20) | No | Current status of the card | Active |

---

# Loans Table

| Column | Data Type | Nullable | Description | Example |
|---------|-----------|----------|-------------|---------|
| loan_id | INT | No | Unique loan identifier | 7001 |
| customer_id | INT | No | Reference to the customer associated with the loan | 1001 |
| loan_type | VARCHAR(30) | No | Type of loan | Home Loan |
| loan_amount | DECIMAL(12,2) | No | Total loan amount | 2500000.00 |
| loan_status | VARCHAR(20) | No | Current status of the loan | Active |

---

# Transactions Table

| Column | Data Type | Nullable | Description | Example |
|---------|-----------|----------|-------------|---------|
| transaction_id | INT | No | Unique transaction identifier | 900001 |
| account_id | INT | No | Reference to the account associated with the transaction | 5001 |
| transaction_type | VARCHAR(20) | No | Type of transaction | Debit |
| amount | DECIMAL(12,2) | No | Transaction amount | 1500.00 |
| transaction_date | DATE | No | Date on which the transaction occurred | 2026-07-29 |

---

# Relationships

The tables are related using customer, account, and branch identifiers.

```text
Customers
    |
    | customer_id
    |
    +------------------+
    |                  |
    v                  v
Accounts             Cards
    |
    | account_id
    |
    v
Transactions

Customers
    |
    | customer_id
    |
    v
Loans

Branches
    |
    | branch_id
    |
    v
Accounts