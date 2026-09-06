# Database Design

## Database Overview

The Financial Data Platform uses a relational PostgreSQL database to store banking data.

The database models six core entities:

- Customers
- Accounts
- Branches
- Cards
- Loans
- Transactions

Primary keys uniquely identify records, while foreign keys establish relationships between related tables.

The design separates customer, account, branch, card, loan, and transaction data into dedicated tables to reduce unnecessary duplication and support SQL-based analysis.

---

# Database Schema

The database consists of the following six tables:

- Customers
- Accounts
- Branches
- Cards
- Loans
- Transactions

The relationships between these tables are established using primary and foreign keys.

---

# Entity Relationship Diagram (ERD)

```text
                         Customers
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              │              │              │
              ▼              ▼              ▼
          Accounts          Loans          Cards
              │
              │
              ▼
        Transactions

Branches
    │
    │ branch_id
    ▼
Accounts