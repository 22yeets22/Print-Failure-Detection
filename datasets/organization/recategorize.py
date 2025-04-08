import os
import shutil


def move_and_rename_images(source_folder, destination_folder):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Get all subfolders inside the source folder
    subfolders = [f for f in os.listdir(source_folder) if os.path.isdir(os.path.join(source_folder, f))]

    image_counter = 1

    for subfolder in subfolders:
        subfolder_path = os.path.join(source_folder, subfolder)

        # Get all images in the subfolder
        images = [f for f in os.listdir(subfolder_path) if os.path.isfile(os.path.join(subfolder_path, f))]

        for image in images:
            # Create a new name for the image
            new_image_name = f"{image_counter:06}.jpg"  # Add appropriate extension based on your image types
            old_image_path = os.path.join(subfolder_path, image)
            new_image_path = os.path.join(destination_folder, new_image_name)

            # Move and rename the image
            shutil.copy(old_image_path, new_image_path)
            image_counter += 1


def scan_and_process_folders():
    # Folder names
    folders = ["p", "n"]

    for folder in folders:
        # Check if the folder exists
        if os.path.exists(folder):
            destination_folder = f"data/{folder}"  # New destination path
            move_and_rename_images(folder, destination_folder)
        else:
            print(f"Folder '{folder}' does not exist!")


if __name__ == "__main__":
    scan_and_process_folders()
