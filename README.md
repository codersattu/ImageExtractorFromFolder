# 🖼️ Image Extractor Tool

A lightweight Python tool that extracts all `.jpg`, `.jpeg`, and `.png` images from a selected folder (including subfolders), and copies them into a new folder named `extracted_images`. Duplicate image names are automatically renamed to avoid overwriting.

## ✨ Features

- ✅ GUI-based folder selection using `tkinter`
- 🔍 Recursively scans all subdirectories
- 🖼️ Extracts `.jpg`, `.jpeg`, `.png` image files
- 📝 Automatically renames duplicate filenames (`image.jpg`, `image_1.jpg`, etc.)
- 📁 All images saved in a clean `extracted_images` folder
- ✅ No external dependencies

## 🚀 How to Use

1. Install Python 3.x if not already installed.
2. Save the script as `image_extractor.py`.
3. Run the script:
   ```bash
   python image_extractor.py```
4. A folder selection window will appear — choose your source folder.
5. Extracted images will be saved in extracted_images inside the selected folder.

## 🖥️ Example Output
Given:
  /photos/folder1/dog.jpg
  /photos/folder2/dog.jpg
  /photos/folder3/cat.png

The tool creates:
  /photos/extracted_images/
  ├── dog.jpg
  ├── dog_1.jpg
  └── cat.png
## 📦 Optional Enhancements
  1. Want to extend this tool? Consider:
  2. Adding support for more image formats like .webp, .gif
  3. Creating a standalone .exe using pyinstaller
  4. Adding a progress bar or log window for larger folders

## 👨‍💻 Author
  Developed by [Abhishek Satpathy] - [abhisat.com]
  Feel free to fork, improve, and share! ❤️




