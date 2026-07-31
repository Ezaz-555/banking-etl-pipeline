import random
import pandas as pd
from faker import Faker

from src.utils.config import RAW_DATA_PATH, NUM_CUSTOMERS

# Faker object
fake = Faker("en_IN")

# Cities
CITIES = [
    "Bangalore",
    "Hyderabad",
    "Chennai",
    "Mumbai",
    "Pune",
    "Delhi",
    "Kolkata",
    "Ahmedabad"
]

# Occupations
OCCUPATIONS = [
    "Software Engineer",
    "Doctor",
    "Teacher",
    "Accountant",
    "Business Owner",
    "Student",
    "Lawyer",
    "Sales Executive",
    "Civil Engineer"
]


def generate_customers(num_customers=NUM_CUSTOMERS):
    """Generate customer data."""

    customers = []

    for customer_id in range(1001, 1001 + num_customers):

        customer = {
            "customer_id": customer_id,
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "date_of_birth": fake.date_of_birth(
                minimum_age=18,
                maximum_age=70
            ),
            "gender": random.choice(["Male", "Female"]),
            "city": random.choice(CITIES),
            "occupation": random.choice(OCCUPATIONS),
            "annual_income": random.randint(300000, 3000000)
        }

        customers.append(customer)

    return pd.DataFrame(customers)


if __name__ == "__main__":

    df = generate_customers()

    print(df.head())
    print(f"\nTotal Customers: {len(df)}")

    df.to_csv(RAW_DATA_PATH / "customers.csv", index=False)

    print("\ncustomers.csv created successfully!")