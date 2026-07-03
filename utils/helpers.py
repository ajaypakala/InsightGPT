"""
InsightGPT
Utility Functions
"""

from datetime import datetime
import pandas as pd


# ==========================================================
# FILE INFORMATION
# ==========================================================

def get_file_name(uploaded_file):
    """
    Returns uploaded file name.
    """
    return uploaded_file.name


def get_file_size(uploaded_file):
    """
    Returns file size in MB.
    """
    return round(uploaded_file.size / (1024 * 1024), 2)


def get_file_extension(uploaded_file):
    """
    Returns file extension.
    """
    return uploaded_file.name.split(".")[-1].lower()


# ==========================================================
# COLUMN HELPERS
# ==========================================================

def get_numeric_columns(df):

    return df.select_dtypes(
        include="number"
    ).columns.tolist()


def get_categorical_columns(df):

    return df.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()


def get_datetime_columns(df):

    return df.select_dtypes(
        include=["datetime64[ns]", "datetime64"]
    ).columns.tolist()


# ==========================================================
# DATA PREVIEW
# ==========================================================

def preview_dataframe(df, rows=10):

    return df.head(rows)


# ==========================================================
# DATASET SUMMARY FOR AI
# ==========================================================

def generate_dataset_summary(df):
    """
    Creates dataset summary for Gemini.
    """

    summary = []

    summary.append("DATASET INFORMATION\n")

    summary.append(f"Rows : {len(df)}")

    summary.append(f"Columns : {len(df.columns)}")

    summary.append(
        f"Missing Values : {int(df.isnull().sum().sum())}"
    )

    summary.append(
        f"Duplicate Rows : {int(df.duplicated().sum())}"
    )

    summary.append("\nCOLUMN NAMES")

    summary.append(", ".join(df.columns))

    summary.append("\nDATA TYPES")

    summary.append(df.dtypes.to_string())

    summary.append("\nSUMMARY STATISTICS")

    try:

        summary.append(
            df.describe(include="all").to_string()
        )

    except Exception:

        pass

    summary.append("\nFIRST FIVE ROWS")

    summary.append(
        df.head().to_string()
    )

    return "\n".join(summary)


# ==========================================================
# FORMAT NUMBERS
# ==========================================================

def format_number(value):

    try:

        value = float(value)

    except Exception:

        return value

    if value >= 1_000_000_000:

        return f"{value/1_000_000_000:.2f}B"

    elif value >= 1_000_000:

        return f"{value/1_000_000:.2f}M"

    elif value >= 1_000:

        return f"{value/1_000:.2f}K"

    else:

        return f"{value:.2f}"


# ==========================================================
# EXPORT CSV
# ==========================================================

def dataframe_to_csv(df):

    return df.to_csv(
        index=False
    ).encode("utf-8")


# ==========================================================
# REPORT NAME
# ==========================================================

def generate_report_filename():

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    return f"InsightGPT_Report_{timestamp}.pdf"


# ==========================================================
# MEMORY USAGE
# ==========================================================

def memory_usage(df):

    return round(

        df.memory_usage(
            deep=True
        ).sum()

        / (1024 * 1024),

        2

    )


# ==========================================================
# MISSING PERCENTAGE
# ==========================================================

def missing_percentage(df):

    return (

        (

            df.isnull().sum()

            /

            len(df)

        )

        * 100

    ).round(2)


# ==========================================================
# UNIQUE VALUES
# ==========================================================

def unique_value_summary(df):

    result = pd.DataFrame({

        "Column": df.columns,

        "Unique Values": [

            df[col].nunique()

            for col in df.columns

        ]

    })

    return result


# ==========================================================
# DATA TYPE SUMMARY
# ==========================================================

def datatype_summary(df):

    result = pd.DataFrame({

        "Column": df.columns,

        "Data Type": df.dtypes.astype(str).values

    })

    return result