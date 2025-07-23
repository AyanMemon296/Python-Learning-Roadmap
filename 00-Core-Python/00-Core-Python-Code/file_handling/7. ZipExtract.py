import os
import zipfile

os.chdir(os.path.dirname(__file__))

ZIP_NAME = "MyFiles.zip"
OUT_DIR = "ExtractedFiles"

os.makedirs(OUT_DIR, exist_ok=True)

with zipfile.ZipFile(ZIP_NAME, "r") as zf:
    zf.extractall(OUT_DIR)

print(f"Extracted all files to {OUT_DIR}/ in script folder.")
