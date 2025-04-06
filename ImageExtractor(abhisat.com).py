import os
import shutil
from tkinter import Tk, filedialog, messagebox

def get_unique_filename(dest_folder, filename):
    """
    Returns a unique filename in the destination folder by appending a counter if needed.
    """
    name, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename

    while os.path.exists(os.path.join(dest_folder, new_filename)):
        new_filename = f"{name}_{counter}{ext}"
        counter += 1

    return new_filename

def extract_images_from_folder():
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory(title="Select a Folder to Extract Images From")

    if not folder_selected:
        messagebox.showinfo("Cancelled", "No folder selected.")
        return

    output_folder = os.path.join(folder_selected, "extracted_images")
    os.makedirs(output_folder, exist_ok=True)

    image_extensions = ('.jpg', '.jpeg', '.png')
    image_count = 0

    for root_dir, _, files in os.walk(folder_selected):
        for file in files:
            if file.lower().endswith(image_extensions):
                full_path = os.path.join(root_dir, file)
                unique_name = get_unique_filename(output_folder, file)
                shutil.copy(full_path, os.path.join(output_folder, unique_name))
                image_count += 1

    messagebox.showinfo("Done", f"Extracted {image_count} image(s) to:\n{output_folder}")

if __name__ == "__main__":
    extract_images_from_folder()
