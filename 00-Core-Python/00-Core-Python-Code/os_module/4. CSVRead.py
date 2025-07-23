import os
import csv

os.chdir(os.path.dirname(__file__))

filename = "Data.csv"

with open(filename, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
