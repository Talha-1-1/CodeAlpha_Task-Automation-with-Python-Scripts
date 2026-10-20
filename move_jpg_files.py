"""
Task 3: Task Automation with Python Scripts
Move all .jpg files from a folder to a new folder

Key Concepts Used:
- os: for folder operations (creating directories, walking through folders)
- shutil: for file moving operations
- file handling: working with file paths and extensions
"""

import os
import shutil


def move_jpg_files(source_folder, destination_folder):
    """
    Move all .jpg files from source folder to destination folder.

    Args:
        source_folder (str): Path to the folder containing .jpg files
        destination_folder (str): Path to the folder where files will be moved
    """
    # Create destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    # Counter for moved files
    moved_count = 0

    # Walk through the source folder recursively
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            # Check if the file has a .jpg extension (case-insensitive)
            if file.lower().endswith('.jpg'):
                # Construct full source and destination paths
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination_folder, file)

                try:
                    # Move the file
                    shutil.move(source_path, destination_path)
                    moved_count += 1
                    print(f"Moved: {file} -> {destination_folder}")
                except Exception as e:
                    print(f"Error moving {file}: {str(e)}")

    # Summary
    if moved_count > 0:
        print(f"\nDone! Successfully moved {moved_count} .jpg file(s).")
    else:
        print("\nNo .jpg files found in the source folder.")


def main():
    """Main function to run the script."""
    print("=" * 50)
    print("  Move .jpg Files to a New Folder")
    print("=" * 50)

    # Read input folders from user
    source_folder = input("\nEnter the source folder path: ").strip()
    destination_folder = input("Enter the destination folder path: ").strip()

    # Validate input
    if not source_folder or not destination_folder:
        print("Error: Both source and destination paths are required.")
        return

    if not os.path.exists(source_folder):
        print(f"Error: Source folder does not exist: {source_folder}")
        return

    # Execute the move
    move_jpg_files(source_folder, destination_folder)


if __name__ == "__main__":
    main()