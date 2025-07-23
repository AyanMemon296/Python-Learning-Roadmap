import os
import csv

os.chdir(os.path.dirname(__file__))

filename = "DataDict.csv"

fieldnames = ["Id", "Product", "Qty"]
rows = [
    {"Id": 1, "Product": "Apples", "Qty": 10},
    {"Id": 2, "Product": "Oranges", "Qty": 5},
    {"Id": 3, "Product": "Bananas", "Qty": 12},
]

with open(filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"{filename} created in {os.getcwd()}")
