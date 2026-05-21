# Developer Toolkit

Tiny developer tools. Built daily. Designed to be useful.

A growing collection of Python utilities, automation scripts, and productivity tools created through consistent daily coding practice.

---

## Current Tools

| Tool               | Description                                         |
| ------------------ | --------------------------------------------------- |
| File Organizer     | Organizes files into folders by file type           |
| Password Generator | Generates secure random passwords                   |
| File Renamer       | Renames files automatically with numbered filenames |
| QR Code Generator  | Generate QR code randomly                   |
| AI File Organizer | Advanced version of file organizer|

---

## Why This Project Exists

This repository is part of my daily coding journey.

Goals:

* Practice Python consistently
* Build useful real-world tools
* Improve automation skills
* Learn clean project structure
* Grow a strong GitHub portfolio

---

## Project Structure

```bash id="t7xjlwm"
developer-toolkit/
│
├── tools/
│   ├── file_organizer.py
│   ├── password_generator.py
│   ├── file_renamer.py
│   └── qr_generator.py
│
├── screenshots/
├── notes/
├── requirements.txt
└── README.md
```

---

## Getting Started

Clone the repository:

```bash id="dsy9j0"
git clone https://github.com/jinniseattle-star/developer-toolkit.git
```

Move into the project folder:

```bash id="0dy90a"
cd developer-toolkit
```

Create virtual environment:

### Mac/Linux

```bash id="dhkqql"
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash id="7x2gsf"
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash id="2lls7x"
pip install -r requirements.txt
```

Run a tool:

```bash id="6chcbk"
python tools/file_organizer.py
```

---

## Future Plans
* Add logging and error handling
* Create more automation tools
* Add screenshots and demos
* Add tests and documentation

---

## Upcoming Tools

* Duplicate File Finder
* Folder Size Analyzer
* CSV Analyzer
* Image Resizer
* PDF Merger

## Tool Details

---

### 5. AI File Organizer

Automatically organizes files into categorized folders such as Images, Documents, Videos, Code, and Archives.

#### Features
- Organizes files by extension
- Automatically creates folders
- Skips hidden/system files
- Handles uncategorized files
- CLI support with Typer

#### Example Usage

```bash
python main.py ~/Downloads

