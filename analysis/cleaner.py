"""
InsightGPT
Data Cleaning Module
"""

import pandas as pd


# ==========================================================
# CLEAN COLUMN NAMES
# ==========================================================

def clean_column_names(df):
    """
    Clean column names.
    """

    df = df.copy()

    df.columns = (
        df.columns.astype(str)
        .str.strip()
        .str.replace(" ", "_", regex=False)
        .str.replace("-", "_", regex=False)
        .str.replace("/", "_", regex=False)
        .str.replace("(", "", regex=False)
        .str.replace(")", "", regex=False)
        .str.lower()
    )

    return df


# ==========================================================
# REMOVE DUPLICATES
# ==========================================================

def remove_duplicates(df):
    """
    Remove duplicate rows.
    """

    return df.drop_duplicates().reset_index(drop=True)


# ==========================================================
# REMOVE EMPTY ROWS
# ==========================================================

def remove_empty_rows(df):
    """
    Remove rows where every value is missing.
    """

    return df.dropna(how="all")


# ==========================================================
# REMOVE EMPTY COLUMNS
# ==========================================================

def remove_empty_columns(df):
    """
    Remove columns where every value is missing.
    """

    return df.dropna(axis=1, how="all")


# ==========================================================
# DETECT DATE COLUMNS
# ==========================================================

def detect_datetime_columns(df):
    """
    Automatically convert date columns.
    """

    df = df.copy()

    for column in df.columns:

        if df[column].dtype == "object":

            try:

                converted = pd.to_datetime(
                    df[column],
                    errors="coerce"
                )

                valid_dates = converted.notna().sum()

                if valid_dates >= len(df) * 0.8:

                    df[column] = converted

            except Exception:

                pass

    return df


# ==========================================================
# FILL MISSING VALUES
# ==========================================================

def fill_missing_values(df):
    """
    Fill missing values automatically.
    """

    df = df.copy()

    for column in df.columns:

        # Numeric Columns

        if pd.api.types.is_numeric_dtype(df[column]):

            median = df[column].median()

            df[column] = df[column].fillna(median)

        # Datetime Columns

        elif pd.api.types.is_datetime64_any_dtype(df[column]):

            # Compatible with Pandas 3.x

            df[column] = df[column].ffill().bfill()

        # Text Columns

        else:

            mode = df[column].mode()

            if not mode.empty:

                df[column] = df[column].fillna(mode.iloc[0])

            else:

                df[column] = df[column].fillna("Unknown")

    return df


# ==========================================================
# COMPLETE CLEANING PIPELINE
# ==========================================================

def clean_dataset(df):
    """
    Complete cleaning pipeline.
    """

    cleaned = df.copy()

    cleaned = clean_column_names(cleaned)

    cleaned = remove_empty_rows(cleaned)

    cleaned = remove_empty_columns(cleaned)

    cleaned = remove_duplicates(cleaned)

    cleaned = detect_datetime_columns(cleaned)

    cleaned = fill_missing_values(cleaned)

    return cleaned


# ==========================================================
# CLEANING REPORT
# ==========================================================

def cleaning_report(original_df, cleaned_df):
    """
    Generate cleaning report.
    """

    report = {

        "Original Rows": len(original_df),

        "Cleaned Rows": len(cleaned_df),

        "Rows Removed":
            len(original_df) - len(cleaned_df),

        "Original Columns":
            original_df.shape[1],

        "Cleaned Columns":
            cleaned_df.shape[1],

        "Missing Values Remaining":
            int(cleaned_df.isnull().sum().sum()),

        "Duplicate Rows Remaining":
            int(cleaned_df.duplicated().sum()),

        "Memory Usage (MB)":
            round(
                cleaned_df.memory_usage(deep=True).sum()
                /
                (1024 * 1024),
                2
            )

    }

    return report