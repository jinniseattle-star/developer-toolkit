import os

def get_size(start_path):

    total_size = 0

    for dirpath, dirnames, filenames in os.walk(start_path):

        for filename in filenames:

            filepath = os.path.join(dirpath, filename)

            # Skip broken symbolic links
            if not os.path.exists(filepath):
                continue

            try:
                total_size += os.path.getsize(filepath)

            except Exception as e:
                print(f"Error reading file: {filepath}")
                print(e)

    return total_size


def format_size(size_bytes):

    for unit in ["B", "KB", "MB", "GB", "TB"]:

        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"

        size_bytes /= 1024

    return f"{size_bytes:.2f} PB"


def analyze_folder(folder_path):

    results = []

    for item in os.listdir(folder_path):

        item_path = os.path.join(folder_path, item)

        if os.path.isdir(item_path):

            size = get_size(item_path)

            results.append((item, size))

    # Sort largest to smallest
    results.sort(key=lambda x: x[1], reverse=True)

    print("\n=== Folder Size Report ===\n")

    for folder_name, size in results:

        readable_size = format_size(size)

        print(f"{folder_name}: {readable_size}")


def main():

    folder_path = input("Enter folder path to analyze: ").strip()

    if not os.path.exists(folder_path):
        print("Error: Folder does not exist.")
        return

    if not os.path.isdir(folder_path):
        print("Error: Path is not a folder.")
        return

    analyze_folder(folder_path)


if __name__ == "__main__":
    main()
