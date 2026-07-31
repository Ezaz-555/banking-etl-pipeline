import random

import pandas as pd

from src.utils.config import (
    RAW_DATA_PATH,
    NUM_CUSTOMERS,
    NUM_CARDS
)

CARD_TYPES = [
    "Debit",
    "Credit"
]

CARD_STATUS = [
    "Active",
    "Blocked",
    "Expired"
]


def generate_cards(num_cards=NUM_CARDS):
    """Generate card data."""

    cards = []

    for card_id in range(9001, 9001 + num_cards):

        card = {
            "card_id": card_id,
            "customer_id": random.randint(1001, 1000 + NUM_CUSTOMERS),
            "card_type": random.choice(CARD_TYPES),
            "expiry_year": random.randint(2027, 2032),
            "card_status": random.choice(CARD_STATUS)
        }

        cards.append(card)

    return pd.DataFrame(cards)


if __name__ == "__main__":

    df = generate_cards()

    print(df.head())
    print(f"\nTotal Cards: {len(df)}")

    df.to_csv(RAW_DATA_PATH / "cards.csv", index=False)

    print("\ncards.csv created successfully!")