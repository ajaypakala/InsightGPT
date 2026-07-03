"""
InsightGPT
Charts Module
"""

import plotly.express as px
import plotly.graph_objects as go


# ==========================================================
# HISTOGRAM
# ==========================================================

def histogram_chart(df, column):

    fig = px.histogram(
        df,
        x=column,
        nbins=30,
        title=f"Histogram - {column}",
        template="plotly_white"
    )

    fig.update_layout(
        xaxis_title=column,
        yaxis_title="Count"
    )

    return fig


# ==========================================================
# BOX PLOT
# ==========================================================

def box_plot(df, column):

    fig = px.box(
        df,
        y=column,
        title=f"Box Plot - {column}",
        template="plotly_white"
    )

    return fig


# ==========================================================
# BAR CHART
# ==========================================================

def bar_chart(df, column):

    data = (
        df[column]
        .value_counts(dropna=False)
        .reset_index()
    )

    data.columns = [column, "Count"]

    fig = px.bar(
        data,
        x=column,
        y="Count",
        text="Count",
        title=f"{column} Distribution",
        template="plotly_white"
    )

    fig.update_traces(
        textposition="outside"
    )

    return fig


# ==========================================================
# PIE CHART
# ==========================================================

def pie_chart(df, column):

    data = (
        df[column]
        .value_counts(dropna=False)
        .reset_index()
    )

    data.columns = [column, "Count"]

    fig = px.pie(
        data,
        names=column,
        values="Count",
        hole=0.45,
        title=f"{column} Distribution"
    )

    return fig


# ==========================================================
# SCATTER PLOT
# ==========================================================

def scatter_chart(df, x_column, y_column):

    fig = px.scatter(
        df,
        x=x_column,
        y=y_column,
        title=f"{y_column} vs {x_column}",
        template="plotly_white"
    )

    return fig


# ==========================================================
# LINE CHART
# ==========================================================

def line_chart(df, x_column, y_column):

    fig = px.line(
        df,
        x=x_column,
        y=y_column,
        markers=True,
        title=f"{y_column} over {x_column}",
        template="plotly_white"
    )

    return fig


# ==========================================================
# CORRELATION HEATMAP
# ==========================================================

def correlation_heatmap(correlation_df):

    fig = go.Figure(
        data=go.Heatmap(
            z=correlation_df.values,
            x=correlation_df.columns,
            y=correlation_df.columns,
            colorscale="Viridis",
            text=correlation_df.round(2).values,
            texttemplate="%{text}",
            hoverongaps=False
        )
    )

    fig.update_layout(
        title="Correlation Heatmap",
        template="plotly_white"
    )

    return fig


# ==========================================================
# MISSING VALUE CHART
# ==========================================================

def missing_values_chart(df):

    missing = df.isnull().sum()

    missing = missing[missing > 0]

    if missing.empty:

        return None

    chart = missing.reset_index()

    chart.columns = [
        "Column",
        "Missing Values"
    ]

    fig = px.bar(
        chart,
        x="Column",
        y="Missing Values",
        text="Missing Values",
        title="Missing Values by Column",
        template="plotly_white"
    )

    return fig


# ==========================================================
# DATA TYPE CHART
# ==========================================================

def data_type_chart(df):

    data = (
        df.dtypes
        .astype(str)
        .value_counts()
        .reset_index()
    )

    data.columns = [
        "Data Type",
        "Count"
    ]

    fig = px.pie(
        data,
        names="Data Type",
        values="Count",
        hole=0.5,
        title="Column Data Types"
    )

    return fig


# ==========================================================
# CORRELATION SCATTER
# ==========================================================

def correlation_scatter(df):

    numeric = df.select_dtypes(
        include="number"
    ).columns.tolist()

    if len(numeric) < 2:

        return None

    fig = px.scatter(
        df,
        x=numeric[0],
        y=numeric[1],
        title=f"{numeric[1]} vs {numeric[0]}",
        template="plotly_white"
    )

    return fig


# ==========================================================
# TIME SERIES CHART
# ==========================================================

def time_series_chart(df, date_column, value_column):

    temp = df.sort_values(date_column)

    fig = px.line(
        temp,
        x=date_column,
        y=value_column,
        markers=True,
        title=f"{value_column} Trend",
        template="plotly_white"
    )

    return fig