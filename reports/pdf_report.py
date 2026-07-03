"""
InsightGPT
PDF Report Generator
"""

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.units import inch


def create_pdf_report(
    filename,
    profile,
    ai_report
):
    """
    Generate PDF report.
    """

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    title_style = styles["Heading1"]
    title_style.alignment = TA_CENTER

    heading = styles["Heading2"]

    normal = styles["BodyText"]

    story = []

    # =====================================================
    # TITLE
    # =====================================================

    story.append(
        Paragraph(
            "InsightGPT - Enterprise AI Data Analysis Report",
            title_style
        )
    )

    story.append(
        Spacer(1, 0.30 * inch)
    )

    # =====================================================
    # DATASET PROFILE
    # =====================================================

    story.append(
        Paragraph(
            "Dataset Profile",
            heading
        )
    )

    story.append(
        Paragraph(
            f"<b>Total Rows:</b> {profile['rows']}",
            normal
        )
    )

    story.append(
        Paragraph(
            f"<b>Total Columns:</b> {profile['columns']}",
            normal
        )
    )

    story.append(
        Paragraph(
            f"<b>Missing Values:</b> {profile['missing']}",
            normal
        )
    )

    story.append(
        Paragraph(
            f"<b>Duplicate Rows:</b> {profile['duplicates']}",
            normal
        )
    )

    story.append(
        Paragraph(
            f"<b>Memory Usage:</b> {profile['memory_mb']} MB",
            normal
        )
    )

    story.append(
        Spacer(1, 0.30 * inch)
    )

    # =====================================================
    # AI REPORT
    # =====================================================

    story.append(
        Paragraph(
            "AI Analysis",
            heading
        )
    )

    for line in ai_report.split("\n"):

        line = line.strip()

        if line == "":

            continue

        story.append(
            Paragraph(
                line,
                normal
            )
        )

    story.append(
        Spacer(1, 0.30 * inch)
    )

    # =====================================================
    # FOOTER
    # =====================================================

    story.append(
        Paragraph(
            "Generated using InsightGPT Enterprise AI Data Analyst",
            normal
        )
    )

    doc.build(story)