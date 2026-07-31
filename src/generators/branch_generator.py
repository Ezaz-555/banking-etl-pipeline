import random

import pandas as pd
from faker import Faker

from src.utils.config import RAW_DATA_PATH, NUM_BRANCHES

# Faker object
fake = Faker("en_IN")

# Branch locations
BRANCHES = [
    ("Bangalore", "Karnataka"),
    ("Hyderabad", "Telangana"),
    ("Chennai", "Tamil Nadu"),
    ("Mumbai", "Maharashtra"),
    ("Pune", "Maharashtra"),
    ("Delhi", "Delhi"),
    ("Kolkata", "West Bengal"),
    ("Ahmedabad", "Gujarat")
]


def generate_branches(num_branches=NUM_BRANCHES):
    """Generate branch data."""

    branches = []

    for branch_id in range(201, 201 + num_branches):

        city, state = random.choice(BRANCHES)

        branch = {
            "branch_id": branch_id,
            "branch_name": f"{city} Branch",
            "city": city,
            "state": state,
            "manager_name": fake.name()
        }

        branches.append(branch)

    return pd.DataFrame(branches)


if __name__ == "__main__":

    df = generate_branches()

    print(df.head())
    print(f"\nTotal Branches: {len(df)}")

    df.to_csv(RAW_DATA_PATH / "branches.csv", index=False)

    print("\nbranches.csv created successfully!")