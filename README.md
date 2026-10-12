# Smart File Organizer

A Python desktop application that organizes files into categorized folders, detects duplicate files, and generates reports through a graphical interface or command-line menu.

## Overview

**Smart File Organizer** helps users manage cluttered folders by automatically sorting files according to their extensions. It also identifies duplicate files using file hashing, moves duplicates into a separate folder, and records application activity.

The project includes a CustomTkinter-based GUI dashboard and a command-line interface (CLI).

## Features

- **Automatic File Organization:** Sort files into categorized folders based on their extensions.
- **Duplicate Detection:** Identify duplicate files using MD5 hashing.
- **Duplicate Management:** Move detected duplicates into a dedicated `Duplicates/` folder.
- **GUI Dashboard:** Interact with the application through a desktop interface.
- **Dark and Light Modes:** Switch between interface themes.
- **Activity Logging:** Record application operations and errors.
- **Report Generation:** Generate reports with file and duplicate information.
- **Modular Architecture:** Keep organization, duplicate detection, reporting, and configuration in separate Python modules.
- **Error Handling:** Handle invalid inputs and common file-operation errors.

## Technology Stack

- **Language:** Python
- **GUI:** CustomTkinter, Pillow
- **File Operations:** `os`, `shutil`
- **Duplicate Detection:** `hashlib`
- **Logging:** `logging`
- **Version Control:** Git and GitHub

## Project Structure

```text
smart-file-organizer/
├── gui/
│   ├── app_ui.py
│   └── assets/
│       └── icons/
├── logs/
│   └── .gitkeep
├── reports/
│   └── .gitkeep
├── test_data/
│   └── README.md
├── config.py
├── duplicate_detector.py
├── main.py
├── organizer.py
├── report_generator.py
├── utils.py
├── requirements.txt
├── project_structure.txt
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

- Python installed on your computer
- Git, if you want to clone the repository

### 1. Clone the repository

```bash
git clone https://github.com/darshitazaveri16-svg/smart-file-organizer.git
cd smart-file-organizer
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can use Command Prompt:

```bat
venv\Scripts\activate.bat
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Launch the graphical interface

```bash
python gui/app_ui.py
```

### Run the command-line interface

```bash
python main.py
```

## How It Works

1. Select a folder to process.
2. Scan files in the selected folder.
3. Identify file categories using their extensions.
4. Move files into the corresponding category folders.
5. Detect duplicate files when the duplicate-detection feature is used.
6. Generate a report and record application activity.

**Important:** Test the application on a sample folder first. File organization and duplicate handling move files on disk, so use a backup when processing important data.

## File Categories

The application uses configured file-extension categories. Depending on the extensions defined in `config.py`, files may be organized into folders such as:

- `Images/`
- `Documents/`
- `Videos/`
- `Music/`
- `Archives/`
- `Code/`
- `Others/`

Check `config.py` for the exact extensions supported by your current version.

## Duplicate Detection

The application uses MD5 hashing to compare file contents. Files with matching hashes are treated as duplicates by the detector.

Detected duplicates can be moved to a `Duplicates/` folder, helping keep the main categorized folders organized.

## Logs and Reports

- **Logs:** Application activity is recorded under `logs/`.
- **Reports:** Generated reports are saved under `reports/`. Report filenames may include timestamps so that multiple reports can be kept separately.

Generated logs and reports are excluded from version control where configured in `.gitignore`.

## Screenshots

Screenshots of the application dashboard, file organization results, and duplicate detection can be added here to demonstrate the interface.

For example, save your screenshots in a `screenshots/` folder and embed them using Markdown:

```markdown
![Smart File Organizer Dashboard](screenshots/dashboard.png)
```

## Future Improvements

- Drag-and-drop folder selection
- More detailed file statistics
- Additional report formats
- Scheduled file organization
- Further improvements to duplicate review and recovery

## Learning Outcomes

This project demonstrates practical experience with:

- Python file handling and automation
- Modular application design
- Hashing and duplicate detection
- GUI development
- Logging and error handling
- Git and GitHub workflows

## Author

**Darshita Zaveri**

## License

This project is intended for educational and learning purposes.