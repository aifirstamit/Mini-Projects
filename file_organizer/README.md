# 📁 File Organizer Using Python Packages and Modules

A Python file organizer that automatically sorts files into separate folders based on their file extensions.

This project demonstrates how to build a reusable Python package using **modules, functions, imports, custom exceptions, file handling, and logging**.

---

## 📌 Project Overview

Managing files in a folder can become difficult when different types of files are mixed together.

This project automatically organizes files into appropriate folders.

For example:

```text
photo.jpg   → Images/
notes.txt   → Text/
report.pdf  → Documents/
data.csv    → Data/
song.mp3    → Audio/
video.mp4   → Videos/
```

The program also handles common file-operation errors such as:

* File or folder not found
* Unsupported file types
* Duplicate filenames
* Permission errors
* Invalid paths
* Operating-system file errors

Every successful and failed operation is recorded in `organizer.log`.

---

## 🎯 Learning Objectives

This project demonstrates:

* Python functions
* Python modules
* Python packages
* Import statements
* File and directory handling
* `pathlib`
* `shutil`
* Exception handling
* Custom exceptions
* Logging
* Duplicate file handling
* Separation of responsibilities

---

## 📂 Project Structure

```text
file_organizer/
│
├── file_organizer/
│   ├── __init__.py
│   ├── detector.py
│   ├── mover.py
│   ├── logger.py
│   └── exceptions.py
│
├── main.py
├── README.md
└── organizer.log
```

### Module Responsibilities

| Module          | Purpose                                  |
| --------------- | ---------------------------------------- |
| `__init__.py`   | Defines the package interface            |
| `detector.py`   | Detects file types and categories        |
| `mover.py`      | Moves files and handles duplicates       |
| `logger.py`     | Records successful and failed operations |
| `exceptions.py` | Contains custom exceptions               |
| `main.py`       | Runs the file organizer                  |
| `organizer.log` | Stores operation logs                    |

---

## 🗂️ Supported File Types

### Images

```text
.jpg
.jpeg
.png
.gif
.webp
```

→ `Images/`

### Documents

```text
.pdf
.doc
.docx
.ppt
.pptx
```

→ `Documents/`

### Text

```text
.txt
.md
```

→ `Text/`

### Data

```text
.csv
.xlsx
.json
```

→ `Data/`

### Videos

```text
.mp4
.avi
.mkv
```

→ `Videos/`

### Audio

```text
.mp3
.wav
```

→ `Audio/`

Files with unsupported extensions are not moved and generate an `UnsupportedFileError`.

---

## ⚙️ How It Works

The application follows this process:

```text
                 Start
                   │
                   ↓
          Read source folder
                   │
                   ↓
             Find a file
                   │
                   ↓
        Detect file extension
                   │
            ┌──────┴──────┐
            │             │
       Supported      Unsupported
            │             │
            ↓             ↓
     Find category    Log failure
            │
            ↓
     Create destination
            │
            ↓
      Check duplicate
            │
       ┌────┴────┐
       │         │
      No        Yes
       │         │
       │         ↓
       │    Create unique
       │       filename
       │         │
       └────┬────┘
            ↓
        Move file
            │
            ↓
       Log operation
            │
            ↓
           End
```

---

## 🚀 Getting Started

### 1. Clone or download the project

Place the project on your computer.

### 2. Open PowerShell

Navigate to the project directory:

```powershell
cd path\to\file_organizer
```

### 3. Create a test folder

```powershell
mkdir test_files
```

### 4. Create sample files

```powershell
New-Item test_files\photo.jpg -ItemType File
New-Item test_files\notes.txt -ItemType File
New-Item test_files\report.pdf -ItemType File
New-Item test_files\data.csv -ItemType File
New-Item test_files\song.mp3 -ItemType File
New-Item test_files\video.mp4 -ItemType File
New-Item test_files\program.exe -ItemType File
```

---

## ▶️ Run the Program

Run:

```powershell
python main.py
```

Example output:

```text
==================================================
          FILE ORGANIZER
==================================================

SUCCESS: photo.jpg -> Images/
SUCCESS: notes.txt -> Text/
SUCCESS: report.pdf -> Documents/
SUCCESS: data.csv -> Data/
SUCCESS: song.mp3 -> Audio/
SUCCESS: video.mp4 -> Videos/
FAILED: program.exe - Unsupported file type: .exe
```

---

## 📁 Result

After running the program, the folder will look like:

```text
test_files/
│
├── Images/
│   └── photo.jpg
│
├── Text/
│   └── notes.txt
│
├── Documents/
│   └── report.pdf
│
├── Data/
│   └── data.csv
│
├── Audio/
│   └── song.mp3
│
├── Videos/
│   └── video.mp4
│
└── program.exe
```

The unsupported `program.exe` remains in the original folder.

---

## ⚠️ Error Handling

The application handles several common errors.

### File Not Found

If the source folder or source file doesn't exist:

```python
FileNotFoundError
```

is raised and the failure is logged.

---

### Unsupported File Type

For unsupported extensions:

```python
class UnsupportedFileError(Exception):
    pass
```

The program reports the unsupported file type and records the failure in the log.

Example:

```text
FAILED: program.exe - Unsupported file type: .exe
```

---

### Duplicate Files

If a destination already contains a file with the same name, the existing file is not overwritten.

For example:

```text
photo.jpg
photo_1.jpg
photo_2.jpg
```

The program automatically generates a unique filename.

---

### Permission Error

If the program does not have permission to access or move a file:

```python
PermissionError
```

is handled and recorded in the log.

---

### Invalid Destination

If the destination path is invalid or is not a directory, the appropriate file-system error is handled and logged.

---

## 📝 Logging

Every successful and failed operation is recorded in:

```text
organizer.log
```

Example:

```text
2026-09-10 16:00:01 - INFO - SUCCESS: Moved 'photo.jpg' to 'Images/photo.jpg'

2026-09-10 16:00:02 - INFO - SUCCESS: Moved 'notes.txt' to 'Text/notes.txt'

2026-09-10 16:00:03 - ERROR - FAILED: Unsupported file type: .exe
```

Logging makes it possible to track what happened during the organization process.

---

## 🧩 Python Concepts Demonstrated

### Function

A function performs a specific task.

Example:

```python
def detect_category(file_path):
    ...
```

---

### Module

A Python file containing related functions and code is called a module.

Examples:

```text
detector.py
mover.py
logger.py
exceptions.py
```

---

### Package

A directory containing related Python modules is a package.

```text
file_organizer/
│
├── __init__.py
├── detector.py
├── mover.py
├── logger.py
└── exceptions.py
```

---

### Import

The package can be imported into `main.py`:

```python
from file_organizer import detect_category
from file_organizer import move_file
```

This allows `main.py` to use functionality defined in separate modules.

---

## 🔄 Separation of Responsibilities

The project follows a simple modular design:

```text
main.py
   │
   ├── detector.py
   │      └── Detect file category
   │
   ├── mover.py
   │      └── Move files
   │
   ├── logger.py
   │      └── Record operations
   │
   └── exceptions.py
          └── Handle custom errors
```

Each module has a specific responsibility rather than putting all functionality into one large Python file.

---

## 🛠️ Technologies Used

* Python 3
* `pathlib`
* `shutil`
* `logging`
* Python packages
* Python modules
* Exception handling

No external Python libraries are required.

---

## 💡 Possible Future Improvements

The project can be extended with:

* Command-line arguments
* User-selected source folders
* More file categories
* Recursive folder organization
* File-size based organization
* Date-based organization
* Dry-run mode
* Configuration file for extensions
* GUI interface
* Undo functionality
* Summary report after organization

---

## 👨‍💻 Author

**AI First**

A Python learning project focused on understanding packages, modules, file handling, and clean code organization.

---

## 📜 License

This project is created for educational and learning purposes.
