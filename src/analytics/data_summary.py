from sqlalchemy import text

from src.utils.config import TABLES
from src.utils.database import engine


def get_table_count(table_name):
    """
    Returns the number of rows in a PostgreSQL table.
    """
    query = text(f"SELECT COUNT(*) FROM {table_name}")

    with engine.connect() as connection:
        result = connection.execute(query)
        return result.scalar()


def execute_scalar_query(query):
    """
    Executes a SQL query that returns a single value.
    """
    with engine.connect() as connection:
        result = connection.execute(text(query))
        return result.scalar()


if __name__ == "__main__":

    print("\n========== DATABASE SUMMARY ==========\n")

    # Row counts
    for _, table_name in TABLES:
        count = get_table_count(table_name)
        print(f"{table_name.capitalize():15}: {count}")

    print("\n========== BUSINESS SUMMARY ==========\n")

    total_balance = execute_scalar_query(
        "SELECT SUM(balance) FROM accounts"
    )

    average_balance = execute_scalar_query(
        "SELECT AVG(balance) FROM accounts"
    )

    print(f"Total Balance      : ₹{total_balance:,.2f}")
    print(f"Average Balance    : ₹{average_balance:,.2f}")

    print("\n======================================")