import os
os.chdir(os.path.dirname(__file__))

# Append Mode: adds text at the end
with open("MyData.txt", "a", encoding="utf-8") as f:
    f.write("This line was appended.\n")

print("Line appended to MyData.txt in script folder.")
