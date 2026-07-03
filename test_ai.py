from ai.ai_service import (
    generate_ai_insights,
    chat_with_data,
    generate_executive_summary,
    generate_marketing_suggestions
)

summary = """
Total Revenue : ₹250000

Average Sale : ₹25000

Highest Sale : ₹65000

Lowest Sale : ₹500

Total Orders : 10

Top Customer : Ajay

Top Product : Laptop

Best Category : Electronics
"""

print("=" * 80)
print("AI BUSINESS INSIGHTS")
print("=" * 80)

print(generate_ai_insights(summary))

print("\n")
print("=" * 80)
print("CHAT WITH DATA")
print("=" * 80)

question = "Who is the highest spending customer?"

print(chat_with_data(summary, question))

print("\n")
print("=" * 80)
print("EXECUTIVE SUMMARY")
print("=" * 80)

print(generate_executive_summary(summary))

print("\n")
print("=" * 80)
print("MARKETING SUGGESTIONS")
print("=" * 80)

print(generate_marketing_suggestions(summary))