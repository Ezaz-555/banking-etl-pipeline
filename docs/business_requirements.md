# Business Requirements

## Introduction

The Financial Data Platform is designed to consolidate banking-related data into a centralized PostgreSQL database.

The platform processes customer, account, branch, card, loan, and transaction datasets using a Python-based ETL pipeline and makes the processed data available for SQL-based analysis.

All datasets used in the project are synthetically generated.

---

# Business Objectives

The primary objectives of this project are:

- Consolidate banking datasets into a centralized database.
- Build a reliable end-to-end ETL pipeline.
- Improve data consistency through validation and duplicate removal.
- Store processed data in a structured PostgreSQL database.
- Enable business analysis using SQL queries.
- Demonstrate practical Data Engineering concepts including ingestion, transformation, validation, loading, logging, and error handling.

---

# Stakeholders

The platform is designed to support analytical use cases for the following business areas.

## Management

Potential needs include:

- Overall customer and account metrics.
- Transaction activity.
- Loan portfolio overview.
- Branch-level performance.

---

## Finance Team

Potential needs include:

- Account balance analysis.
- Transaction summaries.
- Credit and debit activity.
- Loan amount analysis.

---

## Operations Team

Potential needs include:

- Transaction monitoring.
- Account activity analysis.
- Branch activity analysis.
- Data quality monitoring.

---

## Loan Department

Potential needs include:

- Loan portfolio analysis.
- Loan type distribution.
- Loan status analysis.
- Customer-level loan analysis.

---

## Branch Management

Potential needs include:

- Customer distribution by branch.
- Account distribution by branch.
- Transaction activity associated with branches.

---

# Functional Requirements

The platform shall:

- Read banking datasets from CSV files.
- Process each dataset independently.
- Remove duplicate records.
- Validate required fields before loading.
- Load validated data into PostgreSQL.
- Insert new records using PostgreSQL upsert logic.
- Update existing records when primary-key conflicts occur.
- Log pipeline execution details.
- Handle dataset-level processing errors.
- Continue processing unaffected datasets when an error occurs.
- Generate an execution summary after pipeline completion.
- Support SQL-based business analysis.

---

# Non-Functional Requirements

The platform should be:

- Reliable
- Maintainable
- Modular
- Well documented
- Easy to extend
- Consistent
- Accurate
- Suitable for batch processing

The current implementation is designed for the project's synthetic datasets and can be extended in the future for larger-scale processing.

---

# Business Questions

The processed data can be used to answer questions such as:

## Customer Analytics

- How many customers are registered?
- Which cities have the highest number of customers?
- What is the average annual income?
- Which occupations have the most customers?

---

## Account Analytics

- How many accounts exist?
- How many accounts exist by account type?
- Which accounts have the highest balances?
- What is the average account balance?
- What is the total balance across accounts?

---

## Transaction Analytics

- How many transactions exist?
- How many transactions exist by transaction type?
- What is the average transaction amount by transaction type?
- What is the total transaction amount by transaction type?
- Which accounts have the highest transaction activity?
- Which customers have the highest transaction activity?

---

## Loan Analytics

- How many loans exist?
- How many loans exist by loan type?
- How many loans exist by loan status?
- What is the total loan amount?
- Which customers have multiple loans?

---

## Card Analytics

- How many cards exist?
- How many cards exist by card type?
- How many cards are active?
- How many cards exist by card status?

---

## Branch Analytics

- How many branches exist?
- How many accounts are associated with each branch?
- Which branches have the highest account activity?
- How are branches distributed by city and state?

---

# Assumptions

The following assumptions are made for this project:

- All datasets are synthetically generated.
- Currency used for monetary values is INR.
- Each account belongs to a customer.
- A customer can own multiple accounts.
- A customer can own multiple cards.
- A customer can have multiple loans.
- Transactions are associated with accounts.
- The pipeline processes data in batch mode.
- PostgreSQL is used as the target database.
- Primary keys are used to identify unique records.

---

# Project Success Criteria

The project will be considered successful if:

- All six datasets can be ingested successfully.
- Duplicate records are removed during processing.
- Required-field validation is performed.
- Validated data is loaded into PostgreSQL.
- Existing records can be updated through upsert logic.
- Pipeline errors are logged and handled appropriately.
- SQL queries can be used to answer relevant business questions.
- The pipeline produces an execution summary.
- Project documentation accurately describes the implementation.

---

# Expected Deliverables

The project will deliver:

- Synthetic banking datasets
- Python-based ETL pipeline
- Data validation and cleaning logic
- PostgreSQL database
- PostgreSQL upsert logic
- SQL analytical queries
- ETL execution logging
- ETL execution summary
- Project documentation

---

# Future Enhancements

Potential future enhancements include:

- Incremental data loading.
- Additional data quality rules.
- Automated scheduling.
- Cloud storage integration using Amazon S3.
- Workflow orchestration.
- Monitoring and alerting.
- Distributed processing for larger datasets.
- Additional analytical reporting.

These enhancements are not part of the current implementation.

---

# Conclusion

The Financial Data Platform demonstrates an end-to-end batch ETL workflow for banking data.

The current implementation focuses on reliable data ingestion, duplicate removal, required-field validation, PostgreSQL loading, upsert handling, logging, error handling, and SQL-based analysis.

The modular design provides a foundation for extending the platform with cloud storage, orchestration, additional data quality checks, and distributed processing in the future.