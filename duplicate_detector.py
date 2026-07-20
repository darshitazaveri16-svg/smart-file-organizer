import os
import hashlib


def generate_hash(file_path):

    hash_md5 = hashlib.md5()

    try:
        with open(file_path, "rb") as file:

            while chunk := file.read(4096):
                hash_md5.update(chunk)

        return hash_md5.hexdigest()

    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None


def detect_duplicates(folder_path):

    hashes = {}

    duplicates = []

    for root, dirs, files in os.walk(folder_path):

        for file in files:

            file_path = os.path.join(root, file)

            file_hash = generate_hash(file_path)

            if file_hash is None:
                continue

            # If hash already exists → duplicate
            if file_hash in hashes:

                duplicates.append(file_path)

            else:
                hashes[file_hash] = file_path

    # Print duplicates separately
    if duplicates:

        print("\nDuplicate Files Found:\n")

        for duplicate in duplicates:
            print(duplicate)

    else:
        print("\nNo duplicate files found.")

    return duplicates