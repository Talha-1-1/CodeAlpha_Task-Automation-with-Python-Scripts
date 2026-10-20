# Task 3 Requirements - Move .jpg Files

## Task Goal
Automate a small, real-life repetitive task by moving all .jpg files from one folder to a new folder.

## Key Concepts Used ✓

### 1. **os** ✓
- Used for folder operations:
  - `os.makedirs()` - Creates destination folder if it doesn't exist
  - `os.walk()` - Recursively walks through source folder and subfolders
  - `os.path.join()` - Constructs proper file paths
  - `os.path.exists()` - Validates folder existence

### 2. **shutil** ✓
- Used for file operations:
  - `shutil.move()` - Moves files from source to destination

### 3. **File Handling** ✓
- Working with file extensions using `file.lower().endswith('.jpg')`
- Case-insensitive file detection
- Proper path handling with `os.path.join()`

## Implementation Details ✓

### Features Implemented:
- ✓ Creates destination folder if it doesn't exist
- ✓ Recursively searches through subfolders
- ✓ Case-insensitive .jpg detection
- ✓ Error handling for file operations
- ✓ Summary of moved files
- ✓ Input validation

### Files Created:
1. `move_jpg_files.py` - Main automation script
2. `setup_test_files.py` - Test setup helper
3. `README.md` - Documentation
4. `REQUIREMENTS.md` - This file

## Test Results ✓

### Test Setup:
- Created 5 .jpg files in test_source folder (including subfolder)

### Test Execution:
```
Moved: photo1.jpg -> test_destination
Moved: photo2.jpg -> test_destination
Moved: photo3.jpg -> test_destination
Moved: photo4.jpg -> test_destination
Moved: photo5.jpg -> test_destination

Done! Successfully moved 5 .jpg file(s).
```

### Verification:
- ✓ All 5 .jpg files moved successfully
- ✓ Files from subfolders included
- ✓ Source folder preserved structure (only empty subfolder remains)
- ✓ Destination folder contains all moved files

## Usage Example

```bash
python move_jpg_files.py

==================================================
  Move .jpg Files to a New Folder
==================================================

Enter the source folder path: test_source
Enter the destination folder path: test_destination

Moved: photo1.jpg -> test_destination
Moved: photo2.jpg -> test_destination
...
Done! Successfully moved 5 .jpg file(s).
```

## All Requirements Met ✓

The solution successfully automates the repetitive task of moving .jpg files using:
- **os** module for folder operations
- **shutil** module for file moving
- **File handling** for extension detection and path management
- **Error handling** for robust operation
- **User input** for flexibility
- **Recursive folder traversal** for comprehensive coverage