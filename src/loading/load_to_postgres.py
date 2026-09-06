import logging

from sqlalchemy import text

from src.utils.database import engine


logger = logging.getLogger(__name__)


def load_to_postgres(df, table_name):
    """
    Load a cleaned DataFrame into a PostgreSQL table.
    """

    rows_loaded = len(df)

    df.to_sql(
        name=table_name,
        con=engine,
        if_exists="append",
        index=False
    )

    logger.info(f"{table_name} loaded successfully")
    logger.info(f"Rows loaded: {rows_loaded}")


def load_customers(df):
    """
    Insert new customers and update existing customers.
    """

    query = text("""
        INSERT INTO customers (
            customer_id,
            first_name,
            last_name,
            date_of_birth,
            gender,
            city,
            occupation,
            annual_income
        )
        VALUES (
            :customer_id,
            :first_name,
            :last_name,
            :date_of_birth,
            :gender,
            :city,
            :occupation,
            :annual_income
        )
        ON CONFLICT (customer_id)
        DO UPDATE SET
            first_name = EXCLUDED.first_name,
            last_name = EXCLUDED.last_name,
            date_of_birth = EXCLUDED.date_of_birth,
            gender = EXCLUDED.gender,
            city = EXCLUDED.city,
            occupation = EXCLUDED.occupation,
            annual_income = EXCLUDED.annual_income
    """)

    with engine.begin() as connection:

        for _, row in df.iterrows():

            connection.execute(
                query,
                {
                    "customer_id": row["customer_id"],
                    "first_name": row["first_name"],
                    "last_name": row["last_name"],
                    "date_of_birth": row["date_of_birth"],
                    "gender": row["gender"],
                    "city": row["city"],
                    "occupation": row["occupation"],
                    "annual_income": row["annual_income"]
                }
            )

    logger.info(f"Customers processed: {len(df)}")
    logger.info("Customer upsert completed!")


def load_accounts(df):
    """
    Insert new accounts and update existing accounts.
    """

    query = text("""
        INSERT INTO accounts (
            account_id,
            customer_id,
            branch_id,
            account_type,
            balance
        )
        VALUES (
            :account_id,
            :customer_id,
            :branch_id,
            :account_type,
            :balance
        )
        ON CONFLICT (account_id)
        DO UPDATE SET
            customer_id = EXCLUDED.customer_id,
            branch_id = EXCLUDED.branch_id,
            account_type = EXCLUDED.account_type,
            balance = EXCLUDED.balance
    """)

    with engine.begin() as connection:

        for _, row in df.iterrows():

            connection.execute(
                query,
                {
                    "account_id": row["account_id"],
                    "customer_id": row["customer_id"],
                    "branch_id": row["branch_id"],
                    "account_type": row["account_type"],
                    "balance": row["balance"]
                }
            )

    logger.info(f"Accounts processed: {len(df)}")
    logger.info("Account upsert completed!")


def load_branches(df):
    """
    Insert new branches and update existing branches.
    """

    query = text("""
        INSERT INTO branches (
            branch_id,
            branch_name,
            city,
            state,
            manager_name
        )
        VALUES (
            :branch_id,
            :branch_name,
            :city,
            :state,
            :manager_name
        )
        ON CONFLICT (branch_id)
        DO UPDATE SET
            branch_name = EXCLUDED.branch_name,
            city = EXCLUDED.city,
            state = EXCLUDED.state,
            manager_name = EXCLUDED.manager_name
    """)

    with engine.begin() as connection:

        for _, row in df.iterrows():

            connection.execute(
                query,
                {
                    "branch_id": row["branch_id"],
                    "branch_name": row["branch_name"],
                    "city": row["city"],
                    "state": row["state"],
                    "manager_name": row["manager_name"]
                }
            )

    logger.info(f"Branches processed: {len(df)}")
    logger.info("Branch upsert completed!")


def load_cards(df):
    """
    Insert new cards and update existing cards.
    """

    query = text("""
        INSERT INTO cards (
            card_id,
            customer_id,
            card_type,
            expiry_year,
            card_status
        )
        VALUES (
            :card_id,
            :customer_id,
            :card_type,
            :expiry_year,
            :card_status
        )
        ON CONFLICT (card_id)
        DO UPDATE SET
            customer_id = EXCLUDED.customer_id,
            card_type = EXCLUDED.card_type,
            expiry_year = EXCLUDED.expiry_year,
            card_status = EXCLUDED.card_status
    """)

    with engine.begin() as connection:

        for _, row in df.iterrows():

            connection.execute(
                query,
                {
                    "card_id": row["card_id"],
                    "customer_id": row["customer_id"],
                    "card_type": row["card_type"],
                    "expiry_year": row["expiry_year"],
                    "card_status": row["card_status"]
                }
            )

    logger.info(f"Cards processed: {len(df)}")
    logger.info("Card upsert completed!")


def load_loans(df):
    """
    Insert new loans and update existing loans.
    """

    query = text("""
        INSERT INTO loans (
            loan_id,
            customer_id,
            loan_type,
            loan_amount,
            loan_status
        )
        VALUES (
            :loan_id,
            :customer_id,
            :loan_type,
            :loan_amount,
            :loan_status
        )
        ON CONFLICT (loan_id)
        DO UPDATE SET
            customer_id = EXCLUDED.customer_id,
            loan_type = EXCLUDED.loan_type,
            loan_amount = EXCLUDED.loan_amount,
            loan_status = EXCLUDED.loan_status
    """)

    with engine.begin() as connection:

        for _, row in df.iterrows():

            connection.execute(
                query,
                {
                    "loan_id": row["loan_id"],
                    "customer_id": row["customer_id"],
                    "loan_type": row["loan_type"],
                    "loan_amount": row["loan_amount"],
                    "loan_status": row["loan_status"]
                }
            )

    logger.info(f"Loans processed: {len(df)}")
    logger.info("Loan upsert completed!")


def load_transactions(df):
    """
    Insert new transactions and update existing transactions.
    """

    query = text("""
        INSERT INTO transactions (
            transaction_id,
            account_id,
            transaction_type,
            amount,
            transaction_date
        )
        VALUES (
            :transaction_id,
            :account_id,
            :transaction_type,
            :amount,
            :transaction_date
        )
        ON CONFLICT (transaction_id)
        DO UPDATE SET
            account_id = EXCLUDED.account_id,
            transaction_type = EXCLUDED.transaction_type,
            amount = EXCLUDED.amount,
            transaction_date = EXCLUDED.transaction_date
    """)

    with engine.begin() as connection:

        for _, row in df.iterrows():

            connection.execute(
                query,
                {
                    "transaction_id": row["transaction_id"],
                    "account_id": row["account_id"],
                    "transaction_type": row["transaction_type"],
                    "amount": row["amount"],
                    "transaction_date": row["transaction_date"]
                }
            )

    logger.info(f"Transactions processed: {len(df)}")
    logger.info("Transaction upsert completed!")