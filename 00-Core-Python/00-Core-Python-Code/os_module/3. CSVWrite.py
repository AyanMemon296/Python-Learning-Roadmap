import os
import csv

os.chdir(os.path.dirname(__file__))

filename = "Data.csv"
rows = [
    ["Name", "Age", "City"],
    ["Ayan", "23", "Surat"],
    ["User2", "30", "Mumbai"],
    ["User3", "27", "Pune"],
]

with open(filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print(f"{filename} created in {os.getcwd()}")
