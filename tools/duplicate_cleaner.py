import os
import hashlib

def get_file_hash(filepath):
    """
    Generate SHA256 hash for a file.
    """

    sha256 = hashlib.sha256()

    try:
        with open(filepath, "rb") as file:

            while chunk := file.read(4096):
                sha256.update(chunk)

        return sha256.hexdigest()

    except Exception as e:
        print(f"Error reading file: {filepath}")
        print(e)
        return None


def find_duplicates(folder_path):

    hashes = {}
    duplicates = []

    for root, dirs, files in os.walk(folder_path):

        for filename in files:

            filepath = os.path.join(root, filename)

            file_hash = get_file_hash(filepath)

            if not file_hash:
                continue

            if file_hash in hashes:
                duplicates.append(filepath)

            else:
                hashes[file_hash] = filepath

    return duplicates


def delete_duplicates(duplicates):

    if not duplicates:
        print("\nNo duplicate files found.")
        return

    print("\nDuplicate Files Found:\n")

    for index, file in enumerate(duplicates, start=1):
        print(f"{index}. {file}")

    choice = input(
        "\nDo you want to delete these duplicate files? (y/n): "
    ).lower()

    if choice == "y":

        for file in duplicates:

            try:
                os.remove(file)
                print(f"Deleted: {file}")

            except Exception as e:
                print(f"Error deleting {file}")
                print(e)

        print("\nDuplicate cleanup completed.")

    else:
        print("\nNo files were deleted.")


def main():

    print("\n=== Duplicate File Cleaner ===\n")

    folder_path = input("Enter folder path to scan: ").strip()

    if not os.path.exists(folder_path):
        print("Error: Folder does not exist.")
        return

    duplicates = find_duplicates(folder_path)

    delete_duplicates(duplicates)


if __name__ == "__main__":
    main()
