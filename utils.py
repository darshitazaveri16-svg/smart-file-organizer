import os


def get_unique_filename(file_path):

    if not os.path.exists(file_path):
        return file_path

    filename, extension = os.path.splitext(file_path)

    counter = 1

    while True:

        new_file_path = f"{filename}_{counter}{extension}"

        if not os.path.exists(new_file_path):
            return new_file_path

        counter += 1