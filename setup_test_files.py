"""
Setup script to create test files for testing the move_jpg_files.py script.
This creates sample .jpg files in a test source folder.
"""

import os

# Create test directories
os.makedirs("test_source", exist_ok=True)
os.makedirs("test_destination", exist_ok=True)
os.makedirs("test_source/subfolder", exist_ok=True)

# Create sample .jpg files
sample_files = [
    "test_source/photo1.jpg",
    "test_source/photo2.jpg",
    "test_source/photo3.jpg",
    "test_source/subfolder/photo4.jpg",
    "test_source/subfolder/photo5.jpg",
]

# Create the files (empty files for testing)
for file_path in sample_files:
    with open(file_path, 'w') as f:
        f.write("Sample content")

print("Test files created!")
print("\nTest folder structure:")
print("test_source/")
print("  photo1.jpg")
print("  photo2.jpg")
print("  photo3.jpg")
print("  subfolder/")
print("    photo4.jpg")
print("    photo5.jpg")
print("\nYou can now run: python move_jpg_files.py")
print("Source: test_source")
print("Destination: test_destination")