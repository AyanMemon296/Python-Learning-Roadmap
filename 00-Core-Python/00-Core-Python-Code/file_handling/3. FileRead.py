import os
os.chdir(os.path.dirname(__file__))

# Read Mode: read full file as one string
with open("MyData.txt", "r", encoding="utf-8") as f:
    data = f.read()

print("Contents of MyData.txt:")
print(data)
