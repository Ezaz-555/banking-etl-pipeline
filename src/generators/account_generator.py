import random

import pandas as pd

from src.utils.config import (
    RAW_DATA_PATH,
    NUM_ACCOUNTS,
    NUM_CUSTOMERS,
    NUM_BRANCHES
)


ACCOUNT_TYPES = [
    "Savings",
    "Current"
]


def generate_accounts(num_accounts=NUM_ACCOUNTS):
    """Generate account data."""

    accounts = []

    for account_id in range(5001, 5001 + num_accounts):

        account = {
            "account_id": account_id,
            "customer_id": random.randint(1001, 1000 + NUM_CUSTOMERS),
            "branch_id": random.randint(201, 200 + NUM_BRANCHES),
            "account_type": random.choice(ACCOUNT_TYPES),
            "balance": random.randrange(5000, 500001, 1000)
        }

        accounts.append(account)

    return pd.DataFrame(accounts)


if __name__ == "__main__":

    df = generate_accounts()

    print(df.head())
    print(f"\nTotal Accounts: {len(df)}")

    df.to_csv(RAW_DATA_PATH / "accounts.csv", index=False)

    print("\naccounts.csv created successfully!")