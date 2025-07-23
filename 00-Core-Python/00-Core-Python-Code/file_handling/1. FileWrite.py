import os
os.chdir(os.path.dirname(__file__))

# Write Mode: creates file or overwrites it
with open("MyData.txt", "w", encoding="utf-8") as f:
    f.write("Hello from write mode!\n")
    f.write("Line 2.\n")

print("MyData.txt created (or overwritten) in script folder.")
