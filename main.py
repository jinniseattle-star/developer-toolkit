import os
import shutil
import typer
from rich import print

app = typer.Typer()

CATEGORIES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Code": [".py", ".js", ".html", ".css"],
    "Archives": [".zip", ".rar"]
}


@app.command()
def organize(folder_path: str):

    print("\n=== AI File Organizer ===\n")

    # Validate path
    if not os.path.exists(folder_path):
        print("[red]Error: Folder does not exist.[/red]")
        raise typer.Exit()

    if not os.path.isdir(folder_path):
        print("[red]Error: Path is not a folder.[/red]")
        raise typer.Exit()

    files = os.listdir(folder_path)

    organized_count = 0

    for file in files:

        # Skip hidden files
        if file.startswith("."):
            continue

        file_path = os.path.join(folder_path, file)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        extension = os.path.splitext(file)[1].lower()

        moved = False

        # Find matching category
        for category, extensions in CATEGORIES.items():

            if extension in extensions:

                category_folder = os.path.join(folder_path, category)

                os.makedirs(category_folder, exist_ok=True)

                destination = os.path.join(category_folder, file)

                try:
                    shutil.move(file_path, destination)

                    print(f"[green]Moved[/green] {file} → {category}")

                    organized_count += 1
                    moved = True

                except Exception as e:
                    print(f"[red]Error moving {file}: {e}[/red]")

                break

        # Uncategorized files
        if not moved:

            other_folder = os.path.join(folder_path, "Other")

            os.makedirs(other_folder, exist_ok=True)

            destination = os.path.join(other_folder, file)

            try:
                shutil.move(file_path, destination)

                print(f"[blue]Moved[/blue] {file} → Other")

                organized_count += 1

            except Exception as e:
                print(f"[red]Error moving {file}: {e}[/red]")

    print(
        f"\n[bold green]Done! Organized {organized_count} files.[/bold green]"
    )


if __name__ == "__main__":
    app()