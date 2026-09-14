import os
from pathlib import Path

folder = Path("test_downloads")
cateogries = {
    ".jpg" : "Images",
    ".jpeg" : "Images",
    ".png" : "Images",
    ".pdf" : "Documents",
    ".docx" : "Documents",
    ".txt" : "Notes",
    ".csv" : "Spreadsheets",
    ".xlsx" : "Spreadsheets",
}

for item in folder.iterdir():
    if item.is_file():
        extension = item.suffix.lower()
        if extension in cateogries:
            cateogery = cateogries[extension]
        else:
            cateogery = "Others"
        destination_folder = folder/cateogery
        destination_folder.mkdir(exist_ok=True)
        destination = destination_folder/item.name
        item.rename(destination)
        print("Moved",item.name,"->",cateogery)