import logging

logger = logging.getLogger(__name__)


def remove_duplicates(df):
    """
    Remove duplicate rows from the DataFrame.
    """

    original_rows = len(df)

    df = df.drop_duplicates()

    removed_rows = original_rows - len(df)

    logger.info(f"Duplicates removed: {removed_rows}")

    return df