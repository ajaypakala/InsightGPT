import pandas as pd


def retrieve_context(df, question, max_rows=20):
    """
    Retrieve relevant rows based on user question.
    """

    question = question.lower()

    # Search every object column

    object_columns = df.select_dtypes(
        include=["object","category"]
    ).columns

    result = pd.DataFrame()

    for col in object_columns:

        temp = df[
            df[col]
            .astype(str)
            .str.lower()
            .str.contains(question, na=False)
        ]

        result = pd.concat(
            [result, temp]
        )

    result = result.drop_duplicates()

    if len(result) == 0:

        return df.head(max_rows)

    return result.head(max_rows)