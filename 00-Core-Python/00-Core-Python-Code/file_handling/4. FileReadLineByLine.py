import os
os.chdir(os.path.dirname(__file__))

# Read line by line using a loop
with open("MyData.txt", "r", encoding="utf-8") as f:
    for line in f:
        print("LINE:", line.rstrip())
