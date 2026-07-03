def decide_action(question):

    question = question.lower()

    # Charts

    if any(word in question for word in [
        "chart",
        "graph",
        "plot",
        "visualize",
        "trend"
    ]):

        return "chart"

    # Summary

    if any(word in question for word in [
        "summary",
        "overview",
        "describe"
    ]):

        return "summary"

    # Cleaning

    if any(word in question for word in [
        "clean",
        "missing",
        "duplicate",
        "null"
    ]):

        return "cleaning"

    # Correlation

    if any(word in question for word in [
        "correlation",
        "relationship"
    ]):

        return "correlation"

    # Report

    if any(word in question for word in [
        "report",
        "pdf"
    ]):

        return "report"

    return "ai"