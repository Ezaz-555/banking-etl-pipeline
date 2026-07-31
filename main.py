from src.utils.config import TABLES
from src.ingestion.csv_reader import read_csv
from src.transformation.data_cleaner import remove_duplicates
from src.loading.load_to_postgres import load_to_postgres


def main():
    print("Financial Data Platform\n")

    for csv_file, table_name in TABLES:

        print(f"Processing {csv_file}...")

        # Ingestion
        df = read_csv(csv_file)

        # Transformation
        df = remove_duplicates(df)

        # Loading
        load_to_postgres(df, table_name)

    print("\nETL Pipeline completed successfully!")


if __name__ == "__main__":
    main()