import random

import pandas as pd

from src.utils.config import (
    RAW_DATA_PATH,
    NUM_CUSTOMERS,
    NUM_LOANS
)

LOAN_TYPES = [
    "Home",
    "Car",
    "Personal",
    "Education"
]

LOAN_STATUS = [
    "Active",
    "Closed"
]


def generate_loans(num_loans=NUM_LOANS):
    """Generate loan data."""

    loans = []

    for loan_id in range(7001, 7001 + num_loans):

        loan = {
            "loan_id": loan_id,
            "customer_id": random.randint(1001, 1000 + NUM_CUSTOMERS),
            "loan_type": random.choice(LOAN_TYPES),
            "loan_amount": random.randrange(100000, 5000001, 10000),
            "loan_status": random.choice(LOAN_STATUS)
        }

        loans.append(loan)

    return pd.DataFrame(loans)


if __name__ == "__main__":

    df = generate_loans()

    print(df.head())
    print(f"\nTotal Loans: {len(df)}")

    df.to_csv(RAW_DATA_PATH / "loans.csv", index=False)

    print("\nloans.csv created successfully!")