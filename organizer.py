
import os
import shutil
import logging

from config import FILE_CATEGORIES
from utils import get_unique_filename
from duplicate_detector import generate_hash


os.makedirs("logs", exist_ok=True)

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
    folder_path = os.path.abspath(folder_path)

    if not os.path.isdir(folder_path):
        print("Error: Folder does not exist.")
        return

    duplicates_folder = os.path.join(folder_path, "Duplicates")
    os.makedirs(duplicates_folder, exist_ok=True)

    seen_hashes = {}

    # Hash files already in category folders so newly added
    # copies can be recognized on later runs.
    for root, dirs, files in os.walk(folder_path):
        dirs[:] = [
            d for d in dirs
            if d not in {"Duplicates", "reports", "logs"}
        ]

        if os.path.abspath(root) == folder_path:
            continue

        for filename in files:
            path = os.path.join(root, filename)
            file_hash = generate_hash(path)

            if file_hash:
                seen_hashes.setdefault(file_hash, path)

    # Process only files directly inside the selected folder.
    try:
        filenames = os.listdir(folder_path)
    except OSError as error:
        print(f"Cannot access folder: {error}")
        return

    for filename in filenames:
        file_path = os.path.join(folder_path, filename)

        if not os.path.isfile(file_path):
            continue

        try:
            file_hash = generate_hash(file_path)

            if file_hash is None:
                continue

            if file_hash in seen_hashes:
                destination = get_unique_filename(
                    os.path.join(duplicates_folder, filename)
                )
                shutil.move(file_path, destination)
                message = f"Duplicate moved: {filename}"
            else:
                category = get_category(
                    os.path.splitext(filename)[1]
                )
                category_folder = os.path.join(
                    folder_path, category
                )
                os.makedirs(category_folder, exist_ok=True)

                destination = get_unique_filename(
                    os.path.join(category_folder, filename)
                )
                shutil.move(file_path, destination)
                seen_hashes[file_hash] = destination
                message = f"Moved: {filename} -> {category}"

            print(message)
            logging.info(message)

        except (OSError, shutil.Error) as error:
            print(f"Error processing {filename}: {error}")
            logging.exception("Error processing %s", filename)
