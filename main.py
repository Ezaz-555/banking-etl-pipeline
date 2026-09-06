import logging

from src.utils.config import TABLES
from src.ingestion.csv_reader import read_csv
from src.transformation.data_cleaner import remove_duplicates
from src.validation.data_validator import validate_required_fields
from src.loading.load_to_postgres import (
    load_customers,
    load_accounts,
    load_branches,
    load_cards,
    load_loans,
    load_transactions
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


def main():

    logger.info("Financial Data Platform")

    successful_tables = []
    failed_tables = []
    rows_processed = {}

    for csv_file, table_name in TABLES:

        logger.info(f"Processing {csv_file}")

        try:
            # --------------------
            # Ingestion
            # --------------------
            df = read_csv(csv_file)

            # --------------------
            # Transformation
            # --------------------
            df = remove_duplicates(df)

            # --------------------
            # Validation
            # --------------------
            errors = validate_required_fields(df, table_name)

            if errors:
                logger.error(f"Validation failed for {table_name}")

                for error in errors:
                    logger.error(error)

                failed_tables.append(table_name)
                continue

            # --------------------
            # Loading
            # --------------------
            if table_name == "customers":
                load_customers(df)

            elif table_name == "accounts":
                load_accounts(df)

            elif table_name == "branches":
                load_branches(df)

            elif table_name == "cards":
                load_cards(df)

            elif table_name == "loans":
                load_loans(df)

            elif table_name == "transactions":
                load_transactions(df)

            rows_processed[table_name] = len(df)
            successful_tables.append(table_name)

            logger.info(f"{table_name} processed successfully")

        except Exception:
            logger.exception(f"Failed to process {table_name}")
            failed_tables.append(table_name)

    # --------------------
    # Final ETL Summary
    # --------------------
    print("\n" + "=" * 45)
    print("           ETL PIPELINE SUMMARY")
    print("=" * 45)

    for table_name, row_count in rows_processed.items():
        print(f"{table_name:<18}: {row_count} rows")

    print("-" * 45)
    print(f"Successful tables : {len(successful_tables)}")
    print(f"Failed tables     : {len(failed_tables)}")

    if failed_tables:
        print(f"Failed table list : {', '.join(failed_tables)}")
        print("\nETL Pipeline completed with errors.")
    else:
        print("\nETL Pipeline completed successfully!")

    print("=" * 45)


if __name__ == "__main__":
    main()