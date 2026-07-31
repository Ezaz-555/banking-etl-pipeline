# Business Requirements

## Introduction

The Financial Data Platform is designed to centralize financial data from multiple banking systems into a single analytical platform. The platform enables business users to access accurate, consistent, and reliable information for reporting, decision-making, and operational analysis.

The system integrates customer, account, transaction, loan, card, and branch data into a structured PostgreSQL database using an ETL pipeline.

---

# Business Objectives

The primary objectives of this project are:

- Centralize financial data from multiple operational systems.
- Improve reporting and analytical capabilities.
- Provide a single source of truth for financial data.
- Enable business intelligence through SQL analytics.
- Demonstrate an end-to-end Data Engineering pipeline.

---

# Stakeholders

The following business teams will use the platform.

## Executive Management

Needs:

- Overall business performance
- Customer growth
- Revenue trends

---

## Finance Team

Needs:

- Total deposits
- Total withdrawals
- Average account balances
- Transaction summaries

---

## Operations Team

Needs:

- Daily transaction monitoring
- Failed transaction analysis
- Branch activity monitoring

---

## Loan Department

Needs:

- Active loans
- Loan portfolio analysis
- Default monitoring

---

## Branch Managers

Needs:

- Customer count
- Transaction volume
- Branch performance comparison

---

# Functional Requirements

The platform shall:

- Import financial datasets from CSV files.
- Validate incoming records.
- Detect missing or invalid values.
- Remove duplicate records.
- Transform raw data into a standardized format.
- Load processed data into PostgreSQL.
- Support SQL queries for reporting.
- Generate business insights from stored data.

---

# Non-Functional Requirements

The platform should be:

- Reliable
- Scalable
- Maintainable
- Well documented
- Easy to extend
- Consistent
- Accurate
- Modular

---

# Business Questions

The platform should answer the following business questions.

## Customer Analytics

- How many customers are registered?
- Which city has the highest number of customers?
- What is the average annual income?
- Which occupation has the most customers?

---

## Account Analytics

- How many savings accounts exist?
- How many salary accounts exist?
- Which accounts have the highest balances?
- What is the average account balance?

---

## Transaction Analytics

- How many transactions occur daily?
- What is the monthly transaction volume?
- What is the average transaction amount?
- Which transaction channels are most frequently used?
- How many transactions failed?

---

## Loan Analytics

- How many active loans exist?
- What is the total outstanding loan amount?
- Which loan type is most common?
- Which customers have multiple loans?

---

## Card Analytics

- How many debit cards are active?
- How many credit cards are active?
- Which card network is used the most?

---

## Branch Analytics

- Which branch has the highest number of customers?
- Which branch processed the highest transaction volume?
- Which region performs the best?

---

# Assumptions

The following assumptions are made for this project.

- All datasets are synthetically generated.
- Currency used is INR.
- Each account belongs to one customer.
- A customer can own multiple accounts.
- A customer can own multiple cards.
- A customer can have multiple loans.
- Transactions are linked to accounts.
- Data is processed in batch mode.

---

# Project Success Criteria

The project will be considered successful if:

- All datasets are successfully ingested.
- Data quality checks are completed.
- Data is loaded into PostgreSQL.
- SQL queries execute successfully.
- Business questions can be answered accurately.
- Documentation is complete.
- The ETL pipeline is modular and maintainable.

---

# Expected Deliverables

The project will deliver:

- Clean financial datasets
- PostgreSQL database
- ETL pipeline
- SQL analytical queries
- Business reports
- Complete project documentation

---

# Conclusion

The Financial Data Platform aims to demonstrate how financial data can be collected, processed, stored, and analyzed using industry-standard Data Engineering practices. The platform provides a realistic simulation of a modern banking analytics environment and serves as a foundation for reporting, business intelligence, and future enhancements.