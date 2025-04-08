import os

import pytesseract
from icrawler.builtin import BingImageCrawler
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# Define classes and number of images to crawl
searches = {
    "image": 15,
    "3D printer": 15,
    "3D print bed": 10,
    "3D printer head": 5,
    "3D printer nozzle": 5,
}

desired_width = 800
no_text = False


for search, image_count in searches.items():
    # Set up the BingImageCrawler
    folder_name = search.replace(" ", "-")
    bing_crawler = BingImageCrawler(storage={"root_dir": f"p/{folder_name}"})

    # Crawl images
    bing_crawler.crawl(keyword=search, filters=None, max_num=image_count, offset=0)

    # Get the path to the downloaded images
    folder_path = f"p/{folder_name}"  # This should match the root_dir above

    # Resize each image in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            # Open the image
            with Image.open(file_path) as img:
                # Get the original dimensions
                width, height = img.size

                # If the width is larger than the desired width, calculate the new height
                if width > desired_width:
                    aspect_ratio = height / width
                    new_height = int(desired_width * aspect_ratio)
                    img_resized = img.resize((desired_width, new_height))
                else:
                    # Keep original if width is already smaller
                    img_resized = img

                # Extract text using pytesseract to make sure no text is present
                if no_text:
                    text = pytesseract.image_to_string(img_resized)
                    if len(text.strip()) > 4:
                        print(f"Skipping {file_path} due to detected text: {text.strip()}")
                        os.remove(file_path)
                        continue

                new_file_path = file_path.rsplit(".", 1)[0] + ".jpg"
                img_resized.convert("RGB").save(new_file_path)  # overwrite original

        except Exception as e:
            print(f"Error processing {file_path}: {e}")


print("Done, get at:", os.getcwd())
