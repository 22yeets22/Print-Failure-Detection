import os

from PIL import Image


def rename_and_convert_files_in_path(path, base_name="ok", start=1, convert=False):
    # Get all files and sort them
    files = sorted([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])

    for i, filename in enumerate(files, start=start):
        file_path = os.path.join(path, filename)
        ext = os.path.splitext(filename)[1].lower()

        # Create new filename with sequential numbering
        new_name = f"{base_name}{i:06d}"

        if convert and ext in [".png", ".jpeg", ".bmp", ".tiff", ".gif", ".webp"]:
            # Convert image to JPG
            try:
                img = Image.open(file_path)
                # Convert to RGB mode if not already (required for some formats like PNG with transparency)
                if img.mode != "RGB":
                    img = img.convert("RGB")
                new_path = os.path.join(path, new_name + ".jpg")
                img.save(new_path, "JPEG")
                # Remove original file after conversion
                os.remove(file_path)
                print(f"Converted and renamed: {filename} → {new_name}.jpg")
            except Exception as e:
                print(f"Error converting {filename}: {e}")
                # If conversion fails, just rename with original extension
                os.rename(file_path, os.path.join(path, new_name + ext))
        else:
            # Just rename the file keeping the original extension
            os.rename(file_path, os.path.join(path, new_name + ext))
            print(f"Renamed: {filename} → {new_name}{ext}")


path = r"""
C:\Users\lekan.BESTLAPTOP\Visual Studio Code Projects\Print Failure Detection\datasets\p\image
""".strip()
name = "randomimage"
convert = False
rename_and_convert_files_in_path(path, name, start=1, convert=convert)
