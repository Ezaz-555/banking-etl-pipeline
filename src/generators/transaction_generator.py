import random

import pandas as pd

from src.utils.config import (
    RAW_DATA_PATH,
    NUM_ACCOUNTS,
    NUM_TRANSACTIONS
)

TRANSACTION_TYPES = [
    "Deposit",
    "Withdrawal",
    "Transfer"
]


def generate_transactions(num_transactions=NUM_TRANSACTIONS):
    """Generate transaction data."""

    transactions = []

    for transaction_id in range(10001, 10001 + num_transactions):

        transaction = {
            "transaction_id": transaction_id,
            "account_id": random.randint(5001, 5000 + NUM_ACCOUNTS),
            "transaction_type": random.choice(TRANSACTION_TYPES),
            "amount": random.randrange(500, 100001, 500),
            "transaction_date": pd.Timestamp.today().date()
        }

        transactions.append(transaction)

    return pd.DataFrame(transactions)


if __name__ == "__main__":

    df = generate_transactions()

    print(df.head())
    print(f"\nTotal Transactions: {len(df)}")

    df.to_csv(RAW_DATA_PATH / "transactions.csv", index=False)

    print("\ntransactions.csv created successfully!")