import os
os.chdir(os.path.dirname(__file__))

print("Current working folder:")
print(os.getcwd())

print("\nFiles/Folders here:")
print(os.listdir())

folder_name = "TestFolder"
os.makedirs(folder_name, exist_ok=True)
print(f"\nCreated folder: {folder_name} (or already existed).")

with open("Temp.txt", "w", encoding="utf-8") as f:
    f.write("Temp file.\n")
print("Created Temp.txt.")

os.rename("Temp.txt", "Renamed.txt")
print("Renamed Temp.txt -> Renamed.txt")

os.remove("Renamed.txt")
print("Deleted Renamed.txt")
