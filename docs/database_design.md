# Database Design

## Database Overview

The Financial Data Platform uses a relational database model to store and manage banking data. The database is designed using normalization principles to minimize data redundancy, maintain consistency, and improve query performance.

The schema models core banking entities such as customers, accounts, transactions, loans, cards, and branches. Relationships between these entities are established using primary keys and foreign keys to ensure data integrity.

---

# Database Schema

The database consists of the following six tables:

- Customers
- Accounts
- Transactions
- Loans
- Cards
- Branches

Each table represents a specific business entity and is connected through well-defined relationships.

---

# Entity Relationship Diagram (ERD)

```
                        Customers
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼
    Accounts              Loans               Cards
        │
        ▼
 Transactions

 Branches
      │
      ▼
  Accounts
```

---

# Table Descriptions

## Customers

Purpose:

Stores customer personal and demographic information.

Primary Key:

- customer_id

Relationships:

- One customer can own multiple accounts.
- One customer can own multiple loans.
- One customer can own multiple cards.

---

## Accounts

Purpose:

Stores bank account information.

Primary Key:

- account_id

Foreign Keys:

- customer_id → Customers
- branch_id → Branches

Relationships:

- One account belongs to one customer.
- One account belongs to one branch.
- One account can have multiple transactions.

---

## Transactions

Purpose:

Stores all financial transactions performed by customers.

Primary Key:

- transaction_id

Foreign Key:

- account_id → Accounts

Relationships:

- Multiple transactions belong to one account.

---

## Loans

Purpose:

Stores customer loan information.

Primary Key:

- loan_id

Foreign Key:

- customer_id → Customers

Relationships:

- A customer can have multiple loans.

---

## Cards

Purpose:

Stores debit and credit card information.

Primary Key:

- card_id

Foreign Key:

- customer_id → Customers

Relationships:

- A customer can own multiple cards.

---

## Branches

Purpose:

Stores branch information.

Primary Key:

- branch_id

Relationships:

- One branch manages multiple accounts.

---

# Primary Keys

| Table | Primary Key |
|---------|-------------|
| Customers | customer_id |
| Accounts | account_id |
| Transactions | transaction_id |
| Loans | loan_id |
| Cards | card_id |
| Branches | branch_id |

---

# Foreign Keys

| Child Table | Foreign Key | Parent Table |
|--------------|-------------|--------------|
| Accounts | customer_id | Customers |
| Accounts | branch_id | Branches |
| Transactions | account_id | Accounts |
| Loans | customer_id | Customers |
| Cards | customer_id | Customers |

---

# Relationship Summary

| Parent | Child | Relationship |
|----------|--------|--------------|
| Customers | Accounts | One-to-Many |
| Customers | Loans | One-to-Many |
| Customers | Cards | One-to-Many |
| Accounts | Transactions | One-to-Many |
| Branches | Accounts | One-to-Many |

---

# Database Design Principles

The database follows the following design principles:

- Use normalized tables to reduce data redundancy.
- Maintain referential integrity using foreign keys.
- Use surrogate primary keys for efficient joins.
- Store transactional data separately from master data.
- Ensure scalability for future data growth.
- Keep the design modular and easy to maintain.

---

# Conclusion

The database design provides a structured and scalable foundation for the Financial Data Platform. The relational schema supports efficient storage, querying, and analysis of financial data while maintaining data consistency and integrity.