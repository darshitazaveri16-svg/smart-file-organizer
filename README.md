# Smart-File-Organizer
# Smart File Organizer + Duplicate File Detector

## Project Overview

Smart File Organizer is a Python-based automation project that automatically organizes files into categorized folders and detects duplicate files. The project helps users clean messy directories, improve file management, and reduce storage clutter.

This project is built using modular Python architecture and demonstrates practical concepts such as file handling, hashing, logging, automation, and error handling.

---

# Features

* Automatic file organization
* Categorizes files based on extensions
* Creates folders automatically
* Detects duplicate files
* Moves duplicate files to a separate folder
* Logging system for tracking activities
* Report generation system
* Command Line Interface (CLI)
* Error handling for invalid paths and file issues

---

# Folder Structure

```text id="cljlwm"
smart-file-organizer/
│
├── main.py
├── organizer.py
├── duplicate_detector.py
├── report_generator.py
├── utils.py
├── config.py
│
├── logs/
│   └── app.log
│
├── reports/
│   └── report.txt
│
├── test_data/
│
├── requirements.txt
└── README.md
```

---

# Technologies Used

* Python
* os module
* shutil module
* hashlib
* logging
* modular programming

---

# How the Project Works

```text id="9g7r1m"
Select Folder
      ↓
Scan Files
      ↓
Detect File Extensions
      ↓
Categorize Files
      ↓
Create Category Folders
      ↓
Move Files
      ↓
Detect Duplicate Files
      ↓
Move Duplicates
      ↓
Generate Report
      ↓
Save Logs
```

---

# File Categories

The project currently supports:

| Category  | Extensions            |
| --------- | --------------------- |
| Images    | .jpg, .jpeg, .png     |
| Documents | .pdf, .docx, .txt     |
| Videos    | .mp4, .mkv            |
| Music     | .mp3                  |
| Archives  | .zip, .rar            |
| Code      | .py, .html, .css, .js |

Unrecognized files are stored inside:

```text id="g3v8m2"
Others/
```

---

# Duplicate Detection

Duplicate files are detected using:

```text id="f5x1q8"
MD5 Hashing
```

Each file is converted into a unique hash value.
If two files have the same hash:

```text id="n2w7k4"
they are considered duplicates
```

Duplicate files are automatically moved into:

```text id="q9m4x1"
Duplicates/
```

---

# Logging System

Project activities are stored inside:

```text id="1v8q5n"
logs/app.log
```

Logs include:

* moved files
* duplicate files
* errors
* processing details

---

# Report Generation

Reports are automatically generated inside:

```text id="m7x2q9"
reports/report.txt
```

The report contains:

* total scanned files
* duplicate files
* organized files
* processing summary

---

# How To Run the Project

## Step 1 — Clone Repository

```bash id="s4q8m1"
git clone YOUR_GITHUB_REPOSITORY_LINK
```

---

## Step 2 — Open Project Folder

```bash id="4x7n2m"
cd smart-file-organizer
```

---

## Step 3 — Create Virtual Environment

```bash id="p1m9q6"
python -m venv venv
```

---

## Step 4 — Activate Virtual Environment

### Windows

```bash id="k5v2x8"
venv\Scripts\activate
```

---

## Step 5 — Install Dependencies

```bash id="7q1m4x"
pip install -r requirements.txt
```

---

## Step 6 — Run the Project

```bash id="6n3v8q"
python main.py
```

---

# CLI Menu

```text id="r2m7x1"
===================================
 SMART FILE ORGANIZER
===================================

1. Organize Files
2. Detect Duplicate Files
3. Generate Report
4. Exit
```

---

# Example Output

## Organized Files

Before:

```text id="z4m8q2"
test_data/
    photo.jpg
    resume.pdf
    song.mp3
```

After:

```text id="5x1n7m"
test_data/
    Images/
        photo.jpg

    Documents/
        resume.pdf

    Music/
        song.mp3
```

---

# Future Improvements

Future versions may include:

* GUI using Tkinter
* Drag-and-drop support
* AI-based file classification
* Dark mode interface
* CSV/PDF reports
* Real-time monitoring
* File size analytics
* Automatic scheduling

---

# Learning Outcomes

This project helped in learning:

* File handling in Python
* Automation scripting
* Modular project architecture
* Hashing algorithms
* Error handling
* Logging systems
* CLI application development
* Git and GitHub workflow

---

# Author

Developed by Darshita Zaveri

---

# License

This project is for educational and learning purposes.
