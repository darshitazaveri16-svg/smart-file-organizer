import os
import shutil
import logging

from config import FILE_CATEGORIES
from utils import get_unique_filename


# Logging Configuration
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def get_category(extension):

    for category, extensions in FILE_CATEGORIES.items():

        if extension.lower() in extensions:
            return category

    return "Others"


def organize_files(folder_path):

    # Create Duplicates folder
    duplicates_folder = os.path.join(folder_path, "Duplicates")
    os.makedirs(duplicates_folder, exist_ok=True)

    # Dictionary to track file names
    seen_files = {}

    for root, dirs, files in os.walk(folder_path):

        # Skip Duplicates folder itself
        if "Duplicates" in root:
            continue

        for file in files:

            try:

                file_path = os.path.join(root, file)

                # Skip if not a file
                if not os.path.isfile(file_path):
                    continue

                extension = os.path.splitext(file)[1]

                category = get_category(extension)

                category_folder = os.path.join(folder_path, category)

                os.makedirs(category_folder, exist_ok=True)

                # Duplicate detection using filename
                if file in seen_files:

                    duplicate_destination = os.path.join(
                        duplicates_folder,
                        file
                    )

                    duplicate_destination = get_unique_filename(
                        duplicate_destination
                    )

                    shutil.move(file_path, duplicate_destination)

                    print(f"Duplicate moved: {file}")

                    logging.info(f"Duplicate moved: {file}")

                else:

                    seen_files[file] = file_path

                    destination = os.path.join(category_folder, file)

                    destination = get_unique_filename(destination)

                    shutil.move(file_path, destination)

                    print(f"Moved: {file} → {category}")

                    logging.info(f"Moved file: {file}")

            except Exception as e:

                print(f"Error processing file {file}: {e}")

                logging.error(f"Error processing file {file}: {e}")