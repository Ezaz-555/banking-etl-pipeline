import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def read_csv(csv_file):
    csv_path = PROJECT_ROOT / "data" / "raw" / csv_file

    df = pd.read_csv(csv_path)

    return df