import os
import zipfile

os.chdir(os.path.dirname(__file__))

ZIP_NAME = "MyFiles.zip"
FILES_TO_ADD = ["MyData.txt", "MyDataCopy.bin"]

with zipfile.ZipFile(ZIP_NAME, "w") as zf:
    for filename in FILES_TO_ADD:
        if os.path.exists(filename):
            zf.write(filename)
            print(f"Added {filename} to {ZIP_NAME}")
        else:
            print(f"Skip: {filename} not found")

print(f"{ZIP_NAME} created in script folder.")
