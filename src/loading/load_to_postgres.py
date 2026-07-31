from src.utils.database import engine


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

    print(f"\n{'=' * 40}")
    print(f"Table: {table_name}")
    print(f"Rows loaded: {rows_loaded}")
    print("✅ Data loaded successfully!")
    print(f"{'=' * 40}")