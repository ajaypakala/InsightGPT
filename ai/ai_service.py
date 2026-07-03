"""
InsightGPT
AI Service Module
"""

import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# ==========================================================
# LOAD ENVIRONMENT
# ==========================================================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    try:
        API_KEY = st.secrets["GEMINI_API_KEY"]
    except Exception:
        API_KEY = None

if not API_KEY:

    raise ValueError(
        "GEMINI_API_KEY not found in .env file."
    )

client = genai.Client(api_key=API_KEY)

MODEL = "gemini-2.5-flash"


# ==========================================================
# INTERNAL FUNCTION
# ==========================================================

def ask_gemini(prompt: str):

    """
    Sends prompt to Gemini and returns response.
    """

    try:

        response = client.models.generate_content(

            model=MODEL,

            contents=prompt

        )

        return response.text

    except Exception as e:

        return f"❌ Gemini Error:\n\n{e}"


# ==========================================================
# AI DATASET REPORT
# ==========================================================

def generate_ai_insights(dataset_summary):

    prompt = f"""
You are a Senior Data Analyst.

Dataset Information

{dataset_summary}

Generate a professional report.

Include:

1. Dataset Overview

2. Important Insights

3. Data Quality Issues

4. Risks

5. Opportunities

6. Recommendations

7. Executive Summary

Rules

• Never invent values.

• Use only supplied information.

• Use Markdown.
"""

    return ask_gemini(prompt)


# ==========================================================
# CHAT WITH DATA
# ==========================================================

def chat_with_data(dataset_summary, question):

    prompt = f"""
You are an AI Data Analyst.

Dataset Information

{dataset_summary}

User Question

{question}

Instructions

• Answer ONLY using dataset information.

• If information is unavailable,
say so.

• Keep answer concise.

• Use bullet points where appropriate.
"""

    return ask_gemini(prompt)


# ==========================================================
# EXECUTIVE SUMMARY
# ==========================================================

def executive_summary(dataset_summary):

    prompt = f"""
Generate an Executive Summary.

Dataset

{dataset_summary}

Maximum 200 words.

Include

• Overview

• Findings

• Risks

• Recommendations
"""

    return ask_gemini(prompt)


# ==========================================================
# BUSINESS RECOMMENDATIONS
# ==========================================================

def business_recommendations(dataset_summary):

    prompt = f"""
You are a Business Consultant.

Dataset

{dataset_summary}

Generate

• Five Recommendations

• Three Business Risks

• Three Growth Opportunities

• Three Cost Saving Suggestions
"""

    return ask_gemini(prompt)


# ==========================================================
# DATA CLEANING SUGGESTIONS
# ==========================================================

def data_cleaning_suggestions(dataset_summary):

    prompt = f"""
You are a Data Engineer.

Dataset

{dataset_summary}

Suggest

• Missing Value Handling

• Duplicate Removal

• Outlier Detection

• Feature Engineering

• Data Quality Improvements
"""

    return ask_gemini(prompt)


# ==========================================================
# EDA REPORT
# ==========================================================

def eda_report(dataset_summary):

    prompt = f"""
Generate an Exploratory Data Analysis report.

Dataset

{dataset_summary}

Include

• Missing Values

• Data Types

• Numeric Analysis

• Categorical Analysis

• Correlation Suggestions

• Recommended Charts

• Conclusions
"""

    return ask_gemini(prompt)