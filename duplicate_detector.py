
import os
import hashlib


SKIP_FOLDERS = {"Duplicates", "reports", "logs"}


def generate_hash(file_path):
    """Return a SHA-256 hash of a file's contents."""
    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:
            while True:
                chunk = file.read(65536)
                if not chunk:
                    break
                sha256.update(chunk)

        return sha256.hexdigest()

    except OSError as error:
        print(f"Error reading {file_path}: {error}")
        return None


def detect_duplicates(folder_path):
    """Find files with identical content without deleting anything."""
    hashes = {}
    duplicates = []

    for root, dirs, files in os.walk(folder_path):
        dirs[:] = [
            folder for folder in dirs
            if folder not in SKIP_FOLDERS
        ]

        for filename in files:
            file_path = os.path.join(root, filename)
            file_hash = generate_hash(file_path)

            if file_hash is None:
                continue

            if file_hash in hashes:
                duplicates.append(file_path)
            else:
                hashes[file_hash] = file_path

    if duplicates:
        print("\nDuplicate Files Found:\n")
        for path in duplicates:
            print(path)
    else:
        print("\nNo duplicate files found.")

    return duplicates
