"""Parse csv expenses

Step 1: Before running, predict exactly what print(totals) will output.
Step 2: Add a `counts` dict that tracks how many expenses are in each category.
"""

import csv

with open("expenses.csv") as f:
    expenses = list(csv.DictReader(f))

totals = {}
counts = {}
for expense in expenses:
    category = expense["category"]
    totals[category] = totals.get(category, 0) + float(expense["amount"])
    counts[category] = counts.get(category, 0) + 1


print(totals)
print(counts)
