import os

# Folder containing files to rename

folder_path = input("Enter folder path: ")

# New base filename

base_name = input("Enter new filename base: ")

# Get all files

files = os.listdir(folder_path)

# Sort files for consistent numbering

files.sort()

count = 1

for file in files:
old_path = os.path.join(folder_path, file)

```
# Skip folders
if os.path.isdir(old_path):
    continue

# Get file extension
extension = os.path.splitext(file)[1]

# Create new filename
new_name = f"{base_name}_{count}{extension}"

new_path = os.path.join(folder_path, new_name)

# Rename file
os.rename(old_path, new_path)

print(f"Renamed: {file} → {new_name}")

count += 1
```

print("\nDone renaming files!")

