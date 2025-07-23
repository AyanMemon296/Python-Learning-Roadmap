import os
os.chdir(os.path.dirname(__file__))

demo_name = "Sample.txt"

with open(demo_name, "w", encoding="utf-8") as f:
    f.write("Sample file for os.path demo.\n")

joined_path = os.path.join("folderA", "folderB", "data.txt")
print("Joined path:", joined_path)

abs_path = os.path.abspath(demo_name)
print("Absolute path:", abs_path)

print("Exists?:", os.path.exists(demo_name))
print("Dir name:", os.path.dirname(abs_path))
print("Base name:", os.path.basename(abs_path))

root, ext = os.path.splitext(demo_name)
print("File root:", root)
print("File ext:", ext)

print("File size (bytes):", os.path.getsize(demo_name))
