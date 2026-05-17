import os
import shutil

downloads = os.path.expanduser("~/Downloads")

folders = {
    "Images": [".png", ".jpg", ".jpeg"],
    "Videos": [".mp4", ".mov"],
    "Documents": [".pdf", ".docx", ".txt"],
}

for file in os.listdir(downloads):
    filepath = os.path.join(downloads, file)

    if os.path.isfile(filepath):
        ext = os.path.splitext(file)[1].lower()

        for folder, extensions in folders.items():
            if ext in extensions:
                target_folder = os.path.join(downloads, folder)

                os.makedirs(target_folder, exist_ok=True)

                shutil.move(filepath, os.path.join(target_folder, file))
                print(f"Moved {file} → {folder}")
