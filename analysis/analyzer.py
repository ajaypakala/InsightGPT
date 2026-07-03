"""
InsightGPT
Data Analyzer Module
"""

import pandas as pd
import numpy as np


# ==========================================================
# LOAD DATA
# ==========================================================

def load_data(uploaded_file):
    """
    Load CSV file.
    """

    return pd.read_csv(uploaded_file)


# ==========================================================
# DATASET PROFILE
# ==========================================================

def dataset_profile(df):

    profile = {

        "rows": df.shape[0],

        "columns": df.shape[1],

        "missing": int(df.isnull().sum().sum()),

        "duplicates": int(df.duplicated().sum()),

        "memory_mb": round(
            df.memory_usage(deep=True).sum() / (1024 * 1024),
            2
        )

    }

    return profile


# ==========================================================
# COLUMN TYPES
# ==========================================================

def get_numeric_columns(df):

    return df.select_dtypes(
        include=np.number
    ).columns.tolist()


def get_categorical_columns(df):

    return df.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()


def get_datetime_columns(df):

    return df.select_dtypes(
        include=["datetime64[ns]", "datetime64"]
    ).columns.tolist()


def get_boolean_columns(df):

    return df.select_dtypes(
        include="bool"
    ).columns.tolist()


# ==========================================================
# SUMMARY
# ==========================================================

def numerical_summary(df):

    numeric = df.select_dtypes(include=np.number)

    if numeric.empty:

        return pd.DataFrame()

    return numeric.describe().T


def categorical_summary(df, column):

    return (
        df[column]
        .value_counts(dropna=False)
        .reset_index()
        .rename(
            columns={
                "index": column,
                column: "Count"
            }
        )
    )


# ==========================================================
# MISSING VALUES
# ==========================================================

def missing_values(df):

    missing = (

        df.isnull()

        .sum()

        .reset_index()

    )

    missing.columns = [

        "Column",

        "Missing Values"

    ]

    return missing


# ==========================================================
# DATA TYPES
# ==========================================================

def data_types(df):

    types = (

        df.dtypes

        .astype(str)

        .reset_index()

    )

    types.columns = [

        "Column",

        "Data Type"

    ]

    return types


# ==========================================================
# UNIQUE VALUES
# ==========================================================

def unique_values(df):

    unique = (

        df.nunique()

        .reset_index()

    )

    unique.columns = [

        "Column",

        "Unique Values"

    ]

    return unique


# ==========================================================
# COLUMN INFORMATION
# ==========================================================

def column_information(df):

    rows = []

    for column in df.columns:

        rows.append({

            "Column": column,

            "Type": str(df[column].dtype),

            "Missing": int(df[column].isnull().sum()),

            "Unique": int(df[column].nunique())

        })

    return pd.DataFrame(rows)


# ==========================================================
# CORRELATION
# ==========================================================

def correlation_matrix(df):

    numeric = df.select_dtypes(include=np.number)

    if numeric.shape[1] < 2:

        return pd.DataFrame()

    return numeric.corr(numeric_only=True)


# ==========================================================
# SAMPLE DATA
# ==========================================================

def sample_rows(df, rows=5):

    return df.head(rows)


# ==========================================================
# AI SUMMARY
# ==========================================================

def generate_dataset_summary(df):

    summary = []

    summary.append("Dataset Summary\n")

    summary.append(f"Rows: {df.shape[0]}")

    summary.append(f"Columns: {df.shape[1]}")

    summary.append(
        f"Missing Values: {df.isnull().sum().sum()}"
    )

    summary.append(
        f"Duplicate Rows: {df.duplicated().sum()}"
    )

    summary.append("\nColumn Names")

    summary.append(", ".join(df.columns))

    summary.append("\nData Types")

    summary.append(df.dtypes.to_string())

    summary.append("\nStatistics")

    summary.append(

        df.describe(
            include="all"
        ).to_string()

    )

    summary.append("\nFirst Five Rows")

    summary.append(

        df.head().to_string()

    )

    return "\n".join(summary)