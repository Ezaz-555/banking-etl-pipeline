def validate_required_fields(df, table_name):
    """
    Check whether required fields contain NULL values.
    """

    required_columns = {
        "customers": [
            "customer_id"
        ],

        "branches": [
            "branch_id"
        ],

        "accounts": [
            "account_id"
        ],

        "cards": [
            "card_id"
        ],

        "loans": [
            "loan_id"
        ],

        "transactions": [
            "transaction_id",
            "account_id",
            "amount"
        ]
    }

    errors = {}

    columns_to_check = required_columns.get(table_name, [])

    for column in columns_to_check:
        null_count = df[column].isnull().sum()

        if null_count > 0:
            errors[column] = null_count

    return errors