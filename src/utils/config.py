from pathlib import Path

# Project root folder
BASE_DIR = Path(__file__).resolve().parents[2]

# Data folder
RAW_DATA_PATH = BASE_DIR / "data" / "raw"

# Number of records
NUM_CUSTOMERS = 1000
NUM_BRANCHES = 20
NUM_ACCOUNTS = 1500
NUM_LOANS = 300
NUM_CARDS = 1200
NUM_TRANSACTIONS = 5000

# CSV file and PostgreSQL table mapping
TABLES = [
    ("customers.csv", "customers"),
    ("accounts.csv", "accounts"),
    ("branches.csv", "branches"),
    ("cards.csv", "cards"),
    ("loans.csv", "loans"),
    ("transactions.csv", "transactions"),
]