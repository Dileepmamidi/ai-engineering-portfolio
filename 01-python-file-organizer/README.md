# Personal File Organizer

A Python automation project that organizes files into categorized folders based on their file extensions.

## 📌 Problem

A Downloads folder can quickly become difficult to manage when different types of files are mixed together.

For example:

```text
Downloads/
├── image1.jpg
├── image2.png
├── report.pdf
├── resume.pdf
├── notes.txt
├── sales.csv
└── data.json
```

The goal of this project is to automatically organize these files into appropriate folders.

## 🎯 Result

The program transforms the folder into:

```text
Downloads/
├── Images/
│   ├── image1.jpg
│   └── image2.png
│
├── Documents/
│   ├── report.pdf
│   └── resume.pdf
│
├── Notes/
│   └── notes.txt
│
├── Spreadsheets/
│   └── sales.csv
│
└── Others/
    └── data.json
```

## 🛠️ Technologies

* Python
* pathlib

## 🧠 Concepts Practiced

* `Path`
* `Path.iterdir()`
* `Path.is_file()`
* `Path.is_dir()`
* `Path.suffix`
* `Path.name`
* `Path.mkdir()`
* `Path.rename()`
* Dictionaries
* Loops
* Conditional statements
* File-system automation

## 🔍 How It Works

The program:

1. Creates a `Path` object representing the target directory.
2. Iterates through the items in the directory.
3. Checks whether each item is a file.
4. Extracts the file extension.
5. Maps the extension to a category using a dictionary.
6. Creates the destination folder if necessary.
7. Moves the file into the appropriate folder.
8. Places unknown file types into `Others`.

## 💡 Example

```python
categories = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Notes",
    ".csv": "Spreadsheets",
    ".xlsx": "Spreadsheets"
}
```

For a file such as:

```text
report.pdf
```

the program extracts:

```text
.pdf
```

and maps it to:

```text
Documents
```

## 📚 What I Learned

This project introduced me to Python's `pathlib` module and showed how it can be used to work with files and directories in a cleaner, object-oriented way.

I also learned how dictionaries can be used as mappings instead of writing large chains of `if/elif` statements.

## 🚧 Future Improvements

Planned improvements include:

* Duplicate-file handling
* Better error handling
* Logging
* Configurable file categories
* Recursive folder organization
* Command-line arguments
* Dry-run mode
* Undo functionality
* Configuration through JSON
