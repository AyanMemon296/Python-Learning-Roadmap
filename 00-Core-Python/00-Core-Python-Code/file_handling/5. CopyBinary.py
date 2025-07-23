import os
os.chdir(os.path.dirname(__file__))

# Copy a file using binary read/write
SRC = "MyData.txt"
DST = "MyDataCopy.bin"

with open(SRC, "rb") as src_file, open(DST, "wb") as dst_file:
    while True:
        chunk = src_file.read(1024)
        if not chunk:
            break
        dst_file.write(chunk)

print(f"Copied {SRC} to {DST} (binary mode) in script folder.")
