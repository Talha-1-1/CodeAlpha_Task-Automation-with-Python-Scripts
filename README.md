# Task 3: Task Automation with Python Scripts

## Goal
Automate a small, real-life repetitive task by moving all .jpg files from one folder to another.

## Key Concepts Used
- **os**: For folder operations (creating directories, walking through folders)
- **shutil**: For file moving operations
- **File Handling**: Working with file paths and extensions

## Files
- `move_jpg_files.py` - Main script that moves .jpg files
- `setup_test_files.py` - Helper script to create test files
- `README.md` - This documentation file

## How to Use

### Step 1: Create test files (optional)
```bash
python setup_test_files.py
```
This creates sample .jpg files in `test_source` folder.

### Step 2: Run the main script
```bash
python move_jpg_files.py
```

### Step 3: Enter the paths
- Source folder path: Where the .jpg files are located
- Destination folder path: Where you want to move them

## Example
```
Enter the source folder path: test_source
Enter the destination folder path: test_destination
```

Output:
```
Moved: photo1.jpg -> test_destination
Moved: photo2.jpg -> test_destination
Moved: photo3.jpg -> test_destination
Moved: photo4.jpg -> test_destination
Moved: photo5.jpg -> test_destination

Done! Successfully moved 5 .jpg file(s).
```

## Features
- Creates destination folder if it doesn't exist
- Recursively searches through subfolders
- Case-insensitive .jpg detection
- Error handling for file operations
- Summary of moved files"# CodeAlpha_Task-Automation-with-Python-Scripts" 
