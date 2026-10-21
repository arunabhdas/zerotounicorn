"""Expense Totals by Category

Step 1: Before running, predict exactly what print(totals) will output.
Step 2: Add a `counts` dict that tracks how many expenses are in each category.
"""

expenses = [
    {"item": "coffee", "category": "food", "amount": 4.50},
    {"item": "uber", "category": "transport", "amount": 18.00},
    {"item": "lunch", "category": "food", "amount": 15.25},
    {"item": "subway", "category": "transport", "amount": 3.35},
    {"item": "headphones", "category": "stuff", "amount": 89.99},
]

totals = {}
counts = {}
for expense in expenses:
    category = expense["category"]
    totals[category] = totals.get(category, 0) + expense["amount"]
    counts[category] = counts.get(category, 0) + 1

# TODO: build a `counts` dict mapping each category to how many expenses it has

print(totals)
print(counts)
